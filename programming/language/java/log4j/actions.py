#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.makedirs("%s/usr/share/java" % get.installDIR())
    shelltools.move("log4j-1.2.17.jar","%s/usr/share/java" % get.installDIR())
    shelltools.move("log4j-1.2.17-javadoc.jar","%s/usr/share/java" % get.installDIR())
