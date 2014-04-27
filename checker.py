#!env python3

class logger:
    def __init__(self):
        self._success = 0
        self._total = 0

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

    def __str__(self):
        return("%s success on %s tests (%s%%)" % (self._success, self._total, self._success / self._total * 100.0))

class python_checker:
    def check(self, logger):
        import sys
        logger.check(sys.version_info.major > 3 or (sys.version_info.major == 3 and sys.version_info.minor >= 3), "python>=3.3")

class program_checker:
    def check(self, logger):
        import shutil
        
        # use shutil.which when present
        if "which" in dir(shutil):
            w = shutil.which
        else: # fallback to custom made version if it doesn't
            w = self.which

        for p in ["bash", "tcsh", "zsh", "firefox", "chromium", "google-chrome", "gcc", "g++", "clang", "clang++"]:
            logger.check(w(p) is not None, p)

    def which(self, program):
        import os

        for path in [os.path.join(p, program) for p in os.environ["PATH"].split(":")]:
            if os.access(path, os.X_OK):
                return path
        return None

class library_checker:
    def check(self, logger):
        import os, shlex

        libs = self.load("libraries.json")
        
        for lang, conf in libs.items():
            programs = conf["programs"]
            options = conf["options"]
            for file in conf["files"]:
                for p in programs:
                    args = shlex.split(options["file"] % (p, os.path.join("testlib", file["name"])))
                    if "lib" in file:
                        args.append(options["lib"] % file["lib"])

                    c = self.execute(args)
                    logger.check(c, "[%s] check %s with %s" % (lang, file["name"], p))

    def execute(self, args):
        import subprocess

        try:
            p = subprocess.Popen(args, stderr=open("/dev/null", "w"))
            return p.wait() == 0
        except OSError:
            pass
        return False

    def load(self, file):
        import json

        with open(file, "r") as f:
            return json.load(f)

l = logger()
c = python_checker()
c.check(l)
c = program_checker()
c.check(l)
c = library_checker()
c.check(l)

print(l)
