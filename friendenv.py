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

class Env(object):

    def __init__(self, filename):
        self.filename = filename
        self.find_file()
        self.parse_file()

    def find_file(self):
        locations = (os.curdir, os.getcwd(), os.path.expanduser("~"), "/etc")
        for location in locations:
            try:
                file_candidate = os.path.join(location, self.filename)
                if os.access(file_candidate), os.R_OK):
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
            self.config = dict(config)