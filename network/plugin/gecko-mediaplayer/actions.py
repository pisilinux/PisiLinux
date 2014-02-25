#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
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
    pisitools.flags.add("-std=c++11")
    autotools.autoreconf()

    autotools.configure("--disable-schemas-install \
                         --enable-new-libxul \
                         --with-plugin-dir=%s" % plugindir)


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))

