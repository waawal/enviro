from __future__ import generators

try:
    import ConfigParser as configparser
    PY2 = True
except ImportError:
    import configparser
    PY2 = False

class ConfigFileWrapper(object):

    def __init__(self, filename):
        self.fp = open(filename)
        self.section = '[default-section]\n'

    def readline(self):
        if self.section:
            try:
                return self.section
            finally:
                self.section = None
        else:
            return self.fp.readline()

    def __iter__(self):
        for line in self.readline:
            yield line

class Env(object):

    def __init__(self, filename):
        self.filename = filename

    def find_file(self):
        self.filename
        self.file = ConfigFileWrapper(self.filename)

    def parse_file(self):
        config = configparser.ConfigParser()
        if PY2:
            config.readfp(self.file, self.filename)
        else:
            config.read_file(self.file, self.filename)

        self.config = dict(config)