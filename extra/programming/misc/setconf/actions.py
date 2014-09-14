#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("setconf.py")
    pisitools.rename("/usr/bin/setconf.py", "setconf")
    pisitools.doman("setconf.1.gz")
    pisitools.dodoc("COPYING")
