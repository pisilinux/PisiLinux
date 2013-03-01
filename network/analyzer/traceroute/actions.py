#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s" SKIPDIRS="patches"' % (get.CC(),get.CFLAGS()))

def install():
    pisitools.doexe("traceroute/traceroute", "/bin/")
    pisitools.dosym("/bin/traceroute", "/bin/tracert")

    pisitools.doman("traceroute/traceroute.8")
    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS", "README", "TODO")
