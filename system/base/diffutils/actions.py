#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #write sed comands using pisitools.dosed
    shelltools.system('sed -i "/gets is a security hole/d" lib/stdio.in.h')

    # disable automagic libsigsegv dependency
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("ac_cv_libsigsegv", "no")

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-nls")

def build():
    autotools.make('LDFLAGS="%s"' % get.LDFLAGS())

def build():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "README")
