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
    shelltools.export("PYTHON","python2.7")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --disable-maintainer-mode \
                         --enable-fts \
                         --enable-datahub \
                         --enable-telepathy \
                         --enable-downloads-monitor \
                         --enable-explain-queries")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("LC_ALL=en_US.UTF-8")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPY*", "README", "ChangeLog", "NEWS", "AUTHORS")
