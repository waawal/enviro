from __future__ import generators

import os
try:
    import ConfigParser as configparser
    PY3 = False
except ImportError:
    import configparser
    PY3 = True


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
        for line in self.readline():
            yield line

class ConfigFile(object):

    def __init__(self, filename):
        self.filename = filename
        self.locations = (os.getcwd(), os.path.expanduser("~"), "/etc",
                          os.path.dirname(os.path.realpath(__file__)))

    def find_file(self):
        for location in self.locations:
            try:
                file_candidate = os.path.join(location, self.filename)
                if os.access(file_candidate, os.R_OK):
                    self.found_file = file_candidate
                    self.file = ConfigFileWrapper(self.found_file)
                    break
            except IOError:
                continue
        else:
            self.file = None

    def parse_file(self):
        if self.file is None:
            self.config = {}
        else:
            config = configparser.ConfigParser()
            if not PY3:
                config.readfp(self.file, self.filename)
            else:
                config.read_file(self.file, self.filename)
            self._config = dict(config)

    @property
    def config(self):
        self.find_file()
        self.parse_file()
        return self._config

class Env(object):

    def __init__(self, environment):
        self.environment = environment

    def setdefault(self):
        for key, value in self.environment.items():
            os.environ.setdefault(key, val)

def env(filename):
    config_file = ConfigFile(filename)
    environment = Env(config_file.config)