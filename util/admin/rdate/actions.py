#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("RCFLAGS=\"%s %s -DINET6\"" % (get.CFLAGS(),get.LDFLAGS()))

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())
