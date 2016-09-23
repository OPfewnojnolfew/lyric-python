# encoding:utf-8

import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini'))