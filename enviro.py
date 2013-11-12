"""This is the enviro module, you can install it via pypi or simply
drop this file on your pythonpath.

"""


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
    """Since ConfigParser doesn't work with files without sections
    we have to create a "ghost section".

    """

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

class Environment(object):
    """Traverse the paths in LOCATIONS in your quest for the filename.
    load() is the high level method.
    
    """

    LOCATIONS = [os.getcwd(), os.path.expanduser('~'), '/etc',
                 os.path.dirname(os.path.realpath(__main__.__file__))]


    def __init__(self, filename, custom_path=None):
        self.filename = filename
        self.locations = list(self.LOCATIONS)
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
            self.env = {}
        else:
            config = configparser.SafeConfigParser()
            if not PY3:
                config.readfp(self.file, self.filename)
            else:
                config.read_file(self.file, self.filename)
            self.env = dict(config.items('default-section'))

    def setdefault(self):
        for key, value in self.env.items():
            os.environ.setdefault(key, value)

    def load(self):
        self.find_file()
        self.parse_file()
        self.setdefault()
        return self

def setdefault(filename, custom_path=None):
    """Loads a file and sets the setdefault of the environment dict
    to the key-value pairs it finds in the file.

    """
    environment = Environment(filename, custom_path)
    return environment.load()