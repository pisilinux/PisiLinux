#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    shelltools.makedirs("%s/usr/share/java/%s" % (get.installDIR() ,get.srcNAME()))
    shelltools.makedirs("%s/usr/share/icons/hicolor/scalable/apps" % get.installDIR())
    shelltools.move("*.jar", "%s/usr/share/java/%s" % (get.installDIR() ,get.srcNAME()))
    shelltools.move("*.sh", "%s/usr/share/java/%s" % (get.installDIR() ,get.srcNAME()))
    shelltools.move("ext/", "%s/usr/share/java/%s" % (get.installDIR() ,get.srcNAME()))
    shelltools.move("icon/argouml2.svg","%s/usr/share/icons/hicolor/scalable/apps/argouml2.svg" % get.installDIR())
    pisitools.dosym("/usr/share/java/%s/argouml.sh" % get.srcNAME(), "/usr/bin/argouml")
    pisitools.dosym("/usr/share/java/%s/argouml2.sh" % get.srcNAME(), "/usr/bin/argouml2")
    pisitools.dodoc("README.txt")

