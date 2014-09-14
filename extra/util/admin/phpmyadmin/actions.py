#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="phpMyAdmin-%s-all-languages" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/phpmyadmin", "*")

    pisitools.dohtml("*")
    pisitools.dodoc("ChangeLog","LICENSE","README")
