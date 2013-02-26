#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "transfig.3.2.5d"

def setup():
    pisitools.dosed("fig2dev/Imakefile", "\/usr\/local\/lib\/", "/usr/lib/")

    shelltools.system('xmkmf')
    autotools.make('Makefiles')

def build():
    autotools.make("CC=\"%s\" LOCAL_LDFLAGS=\"%s\" CDEBUGFLAGS=\"%s\" USRLIBDIR=/usr/lib" % (get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    autotools.make('install DESTDIR=%s' % get.installDIR())
    pisitools.dosym("/usr/lib/fig2dev/tr_TR.iso8859-9.ps", "/usr/lib/fig2dev/tr_TR.ps")
    pisitools.dodoc("CHANGES", "LATEX.AND.XFIG", "NOTES", "README")
