#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

datadir = "/usr/share/dangerdeep"

def setup():
    pisitools.dosed("SConstruct", "/usr/local/bin", "/usr/bin")
    pisitools.dosed("SConstruct", "/usr/local/share/dangerdeep", datadir)

def build():
    scons.make("usex86sse=2 \
                datadir=%s \
                DESTDIR=%s \
                --cache-disable" % (datadir, get.installDIR()))

def install():
    pisitools.dobin("build/linux/dangerdeep")

    pisitools.insinto("/usr/share/pixmaps", "dftd_icon.png", "dangerdeep.png")
    #pisitools.doman("doc/man/dangerdeep.6")
    pisitools.dodoc("README", "CREDITS", "ChangeLog", "LICENSE")