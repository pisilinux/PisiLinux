#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system('/usr/sbin/apxs -c mod_fastcgi.c fcgi*.c')

def install():
    pisitools.insinto('/usr/lib/apache2/modules', '.libs/mod_fastcgi.so')
