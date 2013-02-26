#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

enetsrc = "src/enet"

def removegames(dest):
    for root, dirs, files in os.walk(dest):
        for name in files:
            if name.startswith("Makefile"):
                pisitools.dosed(os.path.join(root, name), "games/")

def setup():
    # FIXME: do it by hand until pisi actions api change is packaged
    # for i in `find -name "Makefile*"|xargs grep games|sed 's/:.*//g' |cut -c3-|sort -u`;do sed -i -e 's/\/games//g' $i;done
    # removegames("./")

    if shelltools.isDirectory(enetsrc):
        shelltools.unlinkDir(enetsrc)

    shelltools.sym(".", "m4")
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.dobin("src/supertuxkart")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "TODO")

