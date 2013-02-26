#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Don't build acpixtract as a newer one is shipped with acpica
    pisitools.dosed("Makefile", "acpixtract ", "")

def build():
    autotools.make()

def install():
    pisitools.dosbin("acpidump/acpidump")
    pisitools.dobin("madt/madt")

    pisitools.newdoc("madt/README", "README.madt")
    pisitools.dodoc("COPYING", "README")
