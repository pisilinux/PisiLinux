#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="areca"


def install():
    pisitools.dosed("bin/areca_run.sh","JAVADIR=/usr/lib/jvm/java-7-openjdk")
    shelltools.chmod("bin/areca*.sh",0755)
    shelltools.chmod("bin/run_tui.sh",0755)
    shelltools.chmod("areca*.sh",0755)
    pisitools.insinto("/opt/areca/","*")
