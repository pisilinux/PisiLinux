#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_SHARED=ON\
			  -DINSTALL_DOC=ON\
			  -DINSTALL_LOC=ON\
			  -DENABLE_BACKUP=ON \
			  -DWITH_NOKIA_SUPPORT=ON \
			  -DBUILD_PYTHON=/usr/bin/python2.7 \
			  -DWITH_Bluez=ON \
			  -DWITH_IrDA=On \
			  -DINSTALL_BASH_COMPLETION=OFF", installPrefix="%s/usr" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall()

    pisitools.dodoc("ChangeLog", "COPYING", "README")
