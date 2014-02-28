#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/usr/share/fonts/arphic-uming/","*.ttc")
    
    # Create symlinks 
    for conf in shelltools.ls("*.conf"):
        pisitools.insinto("/etc/fonts/conf.avail", "%s" % conf)
        pisitools.dosym("/etc/fonts/conf.avail/%s" % conf, "/etc/fonts/conf.d/%s" % conf)
    
    pisitools.newdoc("license/english/ARPHICPL.TXT", "COPYING")

