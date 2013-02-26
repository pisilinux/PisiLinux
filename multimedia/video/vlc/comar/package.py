#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/lib/vlc/vlc-cache-gen -f /usr/lib/vlc/plugins")

def preRemove():
    for cache in glob.glob("/usr/lib/vlc/plugins/plugins-*-*.dat"):
        try:
            os.unlink(cache)
        except OSError:
            pass
