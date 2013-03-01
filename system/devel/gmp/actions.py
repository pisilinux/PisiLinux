#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    options = "--enable-cxx \
               --enable-mpbsd \
               --enable-fft \
               --localstatedir=/var/state/gmp"

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("ABI", "32")
    else:
        shelltools.export("CCAS","%s -c -Wa,--noexecstack" % get.CC())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.doinfo("doc/*info*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LIB", "NEWS", "README")
