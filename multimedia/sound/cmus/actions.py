#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

contrib = "%s/%s/contrib" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("contrib/*", 0644)
    autotools.rawConfigure("prefix=/usr CONFIG_MIKMOD=y")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto(contrib, "contrib/*")
    pisitools.domove("%s/_cmus" % contrib, "/usr/share/zsh/site-functions/")
    pisitools.dodoc("AUTHORS", "COPYING", "README", "Doc/*.txt")
