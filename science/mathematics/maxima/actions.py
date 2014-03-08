#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-clisp \
                         --mandir=/usr/share/man \
                         --infodir=/usr/share/info \
                         --libexecdir=/usr/lib \
                         --enable-sbcl \
                         --with-default-lisp=sbcl \
                         --with-default-lisp=clisp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")
