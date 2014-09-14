#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "fillets-ng-%s" % get.srcVERSION()

def setup():
    shelltools.export("CPPFLAGS", '-DSYSTEM_DATA_DIR=\"\\\"/usr/share/%s\\\"\"' % get.srcNAME())
    autotools.configure("--with-lua=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO", "COPYING")

