from __future__ import generators
import __main__

import os
try:
    import ConfigParser as configparser
    PY3 = False
except ImportError:
    import configparser
    PY3 = True


class ConfigFileWrapper(object):
    """ Since ConfigParser doesn't work with files without sections
    we have to create a "ghost section". """

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

    def __init__(self, filename, custom_path=None):
        self.filename = filename
        self.locations = [os.getcwd(), os.path.expanduser('~'), '/etc',
                          os.path.dirname(os.path.realpath(__main__.__file__))]
        if not custom_path is None:
            self.locations.insert(0, custom_path)
        self.file = None

    def find_file(self):
        for location in self.locations:
            file_candidate = os.path.join(location, self.filename)
            try:
                if os.access(file_candidate, os.R_OK):
                    print file_candidate
                    self.file_name = file_candidate
                    self.file = ConfigFileWrapper(self.file_name)
                    return
            except (IOError):
                continue

    def parse_file(self):
        if self.file is None:
            self.config = {}
        else:
            config = configparser.SafeConfigParser()
            if not PY3:
                config.readfp(self.file, self.filename)
            else:
                config.read_file(self.file, self.filename)
            self._config = dict(config.items('default-section'))

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
            os.environ.setdefault(key, value)

def setdefault(filename, custom_path=None):
    config_file = ConfigFile(filename, custom_path)
    environment = Env(config_file.config)
    environment.setdefault()