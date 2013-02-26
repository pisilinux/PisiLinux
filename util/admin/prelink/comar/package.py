#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

FILES = ["/var/lib/prelink/full",
         "/var/lib/prelink/quick",
         "/var/lib/prelink/force",
         "/var/log/prelink/prelink.log"]

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for _file in FILES:
        if not os.path.exists(_file):
            f = open(_file, "w")
            f.close()
