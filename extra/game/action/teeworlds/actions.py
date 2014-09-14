#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-b177-r50edfd37-source" % get.srcNAME()
DATADIR = "/usr/share/teeworlds"
NoStrip = [DATADIR]

def setup():
    #shelltools.unlinkDir("src/engine/external/")
    shelltools.cd("../bam-0.4.0")
    shelltools.chmod("make_unix.sh", 0755)
    shelltools.system("./make_unix.sh")

def build():
    shelltools.system('CFLAGS="%s" ../bam-0.4.0/bam -v release' % get.CFLAGS())

def install():
    pisitools.dobin("teeworlds")
    pisitools.dobin("teeworlds_srv")
    pisitools.rename("/usr/bin/teeworlds_srv", "teeworlds-server")

    pisitools.insinto(DATADIR, "data")

    pisitools.dodoc("*.txt")
