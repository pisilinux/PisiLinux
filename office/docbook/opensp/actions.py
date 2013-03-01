#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "OpenSP-%s" % get.srcVERSION()

def setup():
    libtools.gnuconfig_update()
    shelltools.export("ALLOWED_FLAGS", "-O -O1 -O2 -pipe -g")
    autotools.configure("--enable-nls \
                         --enable-http \
                         --disable-doc-build \
                         --disable-static \
                         --enable-default-catalog=/etc/sgml/catalog \
                         --enable-default-search-path=/usr/share/sgml:/usr/share/xml \
                         --datadir=/usr/share/sgml")

def build():
    autotools.make("pkgdocdir=/usr/share/doc/%s" % get.srcNAME())

def install():
    autotools.rawInstall('DESTDIR="%s" pkgdocdir=/usr/share/doc/%s' % (get.installDIR(), get.srcNAME()))

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README")
    pisitools.domove("/usr/share/sgml/locale", "/usr/share")

