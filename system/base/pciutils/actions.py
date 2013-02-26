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

def build():
    autotools.make('OPT="%s" \
                    SHARED="yes" \
                    IDSDIR="/usr/share/misc" \
                    MANDIR="/usr/share/man" \
                    all' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s" \
                          SHARED="yes" \
                          IDSDIR="/usr/share/misc" \
                          MANDIR="/usr/share/man" \
                          install-lib' % get.installDIR())

