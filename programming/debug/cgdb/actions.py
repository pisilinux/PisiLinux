#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("various/rline/src/rline.c", "cgdb_malloc", "malloc")
    autotools.configure()

def build():
    autotools.make()
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")
    pisitools.dohtml("doc/cgdb.html/*")

