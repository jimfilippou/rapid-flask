"""
Contains 'clean()' function and sends it to manager.py
"""

import os
from os.path import join
import time

def clean():
    """
    Cleans the project folder from compiled py files, also seen as .pyc
    """

    class bcolors:
        """
        A list of colors for pretty printing inside terminal
        """
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


    BASEDIR = "/Users/FrozenVortex/Desktop/flask-starter-boilerplate"

    THEN = time.time()

    dirs = [x[0] for x in os.walk(BASEDIR)]

    for directory in dirs:
        reader = os.listdir(directory)
        for item in reader:
            if item.endswith(".pyc"):
                os.remove(join(directory, item))
                print bcolors.OKBLUE + "+ Deleted: %s from %s" % (item, directory) + bcolors.ENDC


    print bcolors.OKGREEN + "+ Done in %s seconds." % round((time.time() - THEN), 2) + bcolors.ENDC
