#!env python3

class logger:
    def __init__(self):
        self.success = 0
        self.total = 0

    def success(self, job):
        self.success += 1
        self.total += 1
        print(job, "[OK]")

    def fail(self, job):
        self.total += 1
        print(job, "[FAIL]")

    def check(self, test, job):
        if test:
            self.success(job)
        else:
            self.fail(job)

    def __str__(self):
        return("%s success on %s tests (%s%%)" % (self.success, self.total, self.success / self.total * 100.0))

class python_checker:
    def check(self, logger):
        import sys
        logger.check(sys.version_info.major > 3 or (sys.version_info.major == 3 and sys.version_info.minor >= 3), "python>=3.3")

class program_checker:
    def check(self, logger):
        import shutil
        for p in ["bash", "tcsh", "zsh", "firefox", "chromium", "google-chrome"]:
            logger.check(shutil.which(p) is not None, p)

l = logger()
c = python_checker()
c.check(l)
p = program_checker()
p.check(l)

print(l)
