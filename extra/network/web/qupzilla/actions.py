#!/usr/bin/python

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("AUTHORS", "README.md")

