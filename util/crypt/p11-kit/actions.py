#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    if get.buildTYPE() == "emul32": options = " --with-module-path=/usr/lib32/pkcs11"
    else: options = " --with-module-path=/usr/lib/pkcs11"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
