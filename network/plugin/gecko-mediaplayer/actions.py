#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# for snapshots only
if "_" in get.srcVERSION():
    WorkDir = "gecko-mediaplayer"

plugindir = "/usr/lib/browser-plugins"

def setup():
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    autotools.configure("--disable-schemas-install \
                         --with-plugin-dir=%s" % plugindir)
                         #--with-xulrunner-sdk \
                         #--enable-new-libxul \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # installing schemas by hand since make install causes sandboxviolations
    # enable only if you are using gconf
    # pisitools.insinto("/etc/gconf/schemas/", "gecko-mediaplayer.schemas")

    pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))

