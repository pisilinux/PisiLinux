#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():
    shelltools.cd("Source")
    shelltools.system("python setup.py configure --enable-debug --verbose --fixed-module-name")

def build():
    autotools.make("-C Source")

def check():
    autotools.make("-C Tests")

def install():
    pisitools.insinto("/usr/lib/%s/site-packages/pysvn" % get.curPYTHON(), "Source/pysvn/__init__.py")
    pisitools.insinto("/usr/lib/%s/site-packages/pysvn" % get.curPYTHON(), "Source/pysvn/_pysvn.so")

    pisitools.dodoc("LICENSE.txt")
