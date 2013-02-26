#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Allow everyone to have full access in /var/tmp/cakephp to be able to update cache
    for root, dirs, files in os.walk("/var/tmp/cakephp"):
        os.system("/bin/chmod 0777 %s" % root)
