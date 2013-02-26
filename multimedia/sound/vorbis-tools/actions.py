#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    autotools.configure('--disable-dependency-tracking \
                         --enable-nls \
                         --enable-vcut \
                         --enable-ogg123 \
                         --with-flac \
                         --with-speex \
                         --with-kate \
                         --docdir="/%s/%s"' % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("CHANGES", "COPYING", "AUTHORS", "README", "ogg123/ogg123rc-example")
