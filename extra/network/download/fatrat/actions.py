#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DWITH_NLS=ON \
                          -DWITH_JABBER=ON \
                          -DWITH_CURL=ON")
    
    jvmdir="/usr/lib/jvm/java-7-openjdk"

def build():
    cmaketools.make()

def install():
    pisitools.dosed("data/defaults.conf", "speed_down=131072", "speed_down=524288")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "LICENSE", "README", "TRANSLATIONS")
