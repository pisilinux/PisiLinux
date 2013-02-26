#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R ntop.ntop /var/lib/ntop")
    os.system("/bin/chown -R ntop.ntop /usr/share/ntop")
