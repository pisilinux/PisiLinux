#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fis")

    #Do not create pyo/pyc
    #pisitools.dosed("wrapper/Makefile.in", "^py_compile.*=.*", "py_compile = /bin/true")

    autotools.configure("--enable-python --disable-static --disable-debug --enable-engine --enable-tools")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS")
