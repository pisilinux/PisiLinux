#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libmemcache-1.4.0.rc2"

def setup():
    for filename in ["README", "NEWS", "AUTHORS"]:
        filename = shelltools.join_path(get.workDIR(), WorkDir, filename)
        shelltools.touch(filename)

    autotools.autoreconf("-fi")
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING")
