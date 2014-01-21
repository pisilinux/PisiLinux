#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("Makefile", "INSTALL.*?STATICLIB", deleteLine=True)
    autotools.make('libdir="/usr/lib" libexecdir="/usr/libexec"')

def install():
    autotools.rawInstall('DESTDIR="%s" libdir="/usr/lib" libexecdir="/usr/libexec"' % get.installDIR())

    pisitools.dodoc("COPYING", "README")