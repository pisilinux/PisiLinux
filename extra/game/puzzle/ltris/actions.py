#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")    # Since we changed configure.in
    shelltools.unlink("po/tr.gmo")
    autotools.configure("--localstatedir=/var/games")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/icons")
    pisitools.insinto("/usr/share/pixmaps", "icons/ltris48.xpm")
    pisitools.domo("po/tr.po", "tr", "ltris.mo")

    pisitools.dodoc("TODO", "ChangeLog", "README", "COPYING", "AUTHORS")
