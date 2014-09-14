#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/usr" % get.installDIR())

    pisitools.remove("/usr/bin/gscriptor")
    pisitools.remove("/usr/share/man/man1/gscriptor.1p.gz")

    pisitools.dodoc("Changelog", "TODO", "README", "LICENCE")
