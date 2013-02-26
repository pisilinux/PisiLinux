#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.popen("/sbin/telinit u &> /dev/null")
