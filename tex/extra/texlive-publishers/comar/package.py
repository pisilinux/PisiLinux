#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    print "texlive: updating the filename database..."
    subprocess.call(["/usr/bin/mktexlsr"])
