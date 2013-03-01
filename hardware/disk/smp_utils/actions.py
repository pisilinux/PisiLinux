#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("CFLAGS='%s -DSMP_UTILS_LINUX'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=%s" % (get.installDIR(), get.defaultprefixDIR()))

    pisitools.dodoc("ChangeLog", "COPYING", "README")
