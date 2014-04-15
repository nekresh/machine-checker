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

l = logger()
c = python_checker()
c.check(l)
p = program_checker()
p.check(l)

print(l)
