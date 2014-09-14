#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

Bindir = "/usr/bin/"

def build():
    pisitools.cflags.add("-Wl,-znoexecstack")
    autotools.make("-j1")

def install():
    pisitools.dobin("src/harvid")
    pisitools.doman("doc/harvid.1")
    
    pisitools.dosym("/usr/bin/ffmpeg", "%s/ffmpeg_harvid" % Bindir)
    pisitools.dosym("/usr/bin/ffprobe", "%s/ffprobe_harvid" % Bindir)

    pisitools.dodoc("COPYING", "ChangeLog")