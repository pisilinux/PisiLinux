#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="SOAPpy-0.12.0"

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog", "PKG-INFO", "LICENSE","README", "TODO")
