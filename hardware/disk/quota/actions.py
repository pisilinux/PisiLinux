#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "quota-tools"

def setup():
    autotools.configure("--enable-ldapmail=try \
                         --enable-rpcsetquota=yes \
                         --enable-rootsbin ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("ROOTDIR=%s" % get.installDIR())

    # remove quotactl.2 as its part of 'man-pages' package
    pisitools.removeDir("/usr/share/man/man2")

    # remove header files as they conflict with glibc
    pisitools.removeDir("/usr/include")

    pisitools.dodoc("README*")
