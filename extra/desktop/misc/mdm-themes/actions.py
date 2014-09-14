#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

BuildDir = "usr/share/mdm/themes/"
datadir = "/usr/share/mdm/themes"


def install():
    shelltools.cd(BuildDir)
    for dir in ["Arc-Brave-Userlist", "Arc-Dust-Userlist", "Arc-Human-Userlist", 
                "Arc-Illustrious-Userlist" ,"Arc-Noble-Userlist", "Arc-Wine-Userlist", "Arc-Wise-Userlist", "Dark"]:
        pisitools.insinto(datadir, dir)
        
    shelltools.cd("../../../..")   
    shelltools.cd("debian")   

    pisitools.dodoc("changelog", "copyright")
