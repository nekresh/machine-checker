#!env python3

class logger:
    def __init__(self, verbose=False):
        self._success = 0
        self._total = 0
        self._verbose = verbose

    def success(self, job):
        self._success += 1
        self._total += 1
        print(job, "[OK]")

    def fail(self, job):
        self._total += 1
        print(job, "[FAIL]")

    def check(self, test, job):
        if test:
            self.success(job)
        else:
            self.fail(job)

    def verbose(self, cmd):
        if self._verbose:
            print(cmd)

    def __str__(self):
        return("%s success on %s tests (%.5s%%)" % (self._success, self._total, self._success / self._total * 100.0))

class python_checker:
    def __init__(self, logger):
        self._logger = logger

    def check(self, mode):
        import sys
        self._logger.check(sys.version_info.major > 3 or (sys.version_info.major == 3 and sys.version_info.minor >= 3), "python>=3.3")

class program_checker:
    def __init__(self, logger):
        self._logger = logger

    def check(self, mode):
        import shutil, os
        
        # use shutil.which when present
        if "which" in dir(shutil):
            w = shutil.which
        else: # fallback to custom made version if it doesn't
            w = self.which

        binaries = []
        with open(os.path.join("programs", "common.programs"), "r") as f:
            for l in f:
                binaries.append(l.strip())

        try:
            with open(os.path.join("programs", "%s.programs" % mode), "r") as f:
                for l in f:
                    binaries.append(l.strip())
        except:
            self._logger.fail("mode %s" % mode)
            pass

        for p in binaries:
            self._logger.check(w(p) is not None, p)

    def which(self, program):
        import os

        for path in [os.path.join(p, program) for p in os.environ["PATH"].split(":")]:
            if os.access(path, os.X_OK):
                return path
        return None

class library_checker:
    def __init__(self, logger):
        self._logger = logger

    def check(self, mode):
        import os, shlex

        libs = self.load(os.path.join("testlib", "libraries.json"))
        
        for lang, conf in libs.items():
            programs = conf["programs"]
            options = conf["options"]
            for file in conf["files"]:
                for p in programs:
                    args = shlex.split(options["file"] % (p, os.path.join("testlib", lang, file["name"])))

                    for key in file:
                        if not key == "name":
                            tmp = self.getAdditionalArgs(key, file, options)
                            for item in tmp:
                                args.append(item)

                    c = self.execute(args)
                    self._logger.check(c, "[%s] check %s with %s" % (lang, file["name"], p))

    def getAdditionalArgs(self, key, file, options):
        import shlex
        entry = file[key]
        
        if type(entry) is dict and "$exec" in entry:
            import subprocess
            args = shlex.split(entry["$exec"])

            try:
                with open("/dev/null", "w") as stderr:
                    output = subprocess.check_output(args, stderr=stderr).decode("ascii")
            except OSError:
                output = ""
            except subprocess.CalledProcessError:
                output = ""

            return shlex.split(output)
        elif type(entry) is list:
            return [ options[key] % item for item in entry ]
        elif key in options:
            return [ options[key] % file[key] ]

        return shlex.split(file[key])

    def execute(self, args):
        import subprocess

        self._logger.verbose(' '.join(args))
        try:
            p = subprocess.Popen(args, stderr=subprocess.DEVNULL)
            value = p.wait() == 0
            self._logger.verbose("ret: %s" % value)
            return value
        except OSError:
            pass
        return False

    def load(self, file):
        import json

        with open(file, "r") as f:
            return json.load(f)

class manpage_checker:
    def __init__(self, logger):
        self._logger = logger

    def check(self, mode):
        import os

        manpages = self.load(os.path.join("mans", "manpages.json"))

        for category, pages in manpages.items():
            for page in pages:
                c = self.execute(category, page)
                self._logger.check(c, "[man] %s %s" % (category, page))

    def execute(self, category, page):
        import subprocess

        self._logger.verbose("man %s %s" % (category, page))
        try:
            p = subprocess.Popen(["man", category, page], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return p.wait() == 0
        except OSError:
            pass
        return False

    def load(self, file):
        import json

        with open(file, "r") as f:
            return json.load(f)

def main(args):
    import getopt

    mode = "std"
    if len(args) > 1:
        mode = args[1]

    l = logger()
    c = python_checker(l)
    c.check(mode)
    c = program_checker(l)
    c.check(mode)
    c = library_checker(l)
    c.check(mode)
    c = manpage_checker(l)
    c.check(mode)
    
    print(l)

if __name__ == "__main__":
    import sys
    main(sys.argv)
