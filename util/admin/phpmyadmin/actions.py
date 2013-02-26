#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="phpMyAdmin-%s-all-languages" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/phpmyadmin", "*")

    pisitools.dohtml("*")
    pisitools.dodoc("ChangeLog","CREDITS","Documentation.txt","LICENSE","README")
