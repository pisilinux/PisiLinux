#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make()
    getweb = ['cpwl','2200','2300','2430','1000','1005','1018','1020','1025','1215','1500','1600','2600n','1600w','1680','1690','2480','2490','2530','4690','110','6115','6121','300','315','325','365','600','610','2160','3160','3175','3185','6110','500','301','c310','3200','3300','3400','3530','5100','5200','5500','5600','5800','160','1000','1005','1018','1020','P1005','P1006','P1007','P1008','P1505']
    for i in range(len(getweb)):
        shelltools.system("./getweb %s" % getweb[i])
    #autotools.make("cups")
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README","COPYING","INSTALL")

