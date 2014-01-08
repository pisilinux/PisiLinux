#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    #package name change
    pisitools.dosed("mate-system-monitor.desktop.in*", "_Name=MATE System Monitor", "_Name=System Monitor")
    autotools.configure("--disable-static \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")