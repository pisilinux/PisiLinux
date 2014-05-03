#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    os.system("/bin/chmod g+s /usr/lib/kde4/libexec/kdesud")
    os.system("/bin/chown :nobody /usr/lib/kde4/libexec/kdesud")