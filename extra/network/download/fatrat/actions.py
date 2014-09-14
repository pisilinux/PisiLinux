#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DWITH_NLS=ON \
                          -DWITH_JABBER=ON \
                          -DWITH_WEBINTERFACE=ON \
                          -DWITH_BITTORRENT=ON \
                          -DWITH_CURL=ON")

def build():
    cmaketools.make()

def install():
    pisitools.dosed("data/defaults.conf", "speed_down=131072", "speed_down=524288")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "LICENSE", "README", "TRANSLATIONS")
