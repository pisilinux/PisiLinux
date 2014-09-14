#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("HELP")
