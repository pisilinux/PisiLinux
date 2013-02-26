#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("README.txt","ChangeLog.txt", "COPYING", "JSON.txt")
