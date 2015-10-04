import time

class Timer(object):
    def __init__(self, description=None):
        self.description = description

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.s = self.end - self.start
        self.ms = self.s * 1000
        if self.description:
            print('elapsed time %s: %f s' % (self.description, self.s))
