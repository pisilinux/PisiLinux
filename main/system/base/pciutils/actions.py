#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

