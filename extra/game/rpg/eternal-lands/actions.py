#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ='elc'

datadir = "/usr/share/eternal-lands"

def setup():
    pisitools.dosed("Makefile.linux", "-O0 -ggdb", "%s -DUSE_ACTOR_DEFAULTS" % get.CFLAGS())

def build():
    autotools.make("-f Makefile.linux")

def install():
    pisitools.dobin("el.x86.linux.bin")
    pisitools.rename("/usr/bin/el.x86.linux.bin", "eternal-lands")

    pisitools.insinto(datadir, "*.ini")

    pisitools.dohtml("docs/eye_candy/*")
    pisitools.dodoc("CHANGES", "TODO", "*.txt")
