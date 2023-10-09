#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean
"""
from fabric.api import *
from datetime import datetime
import os
from os.path import exists, isfile

env.hosts = ['100.25.19.204', '54.157.159.85']

def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]