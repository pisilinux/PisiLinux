#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

D = {"target": get.installDIR(),
     "cflags": "%s -fno-strict-aliasing" % get.CFLAGS(),
     "docdir": "%s/%s" % (get.docDIR(), get.srcNAME())}

def fixflags(d):
    for root, dirs, files in os.walk(d):
        for name in files:
            if name == "Makefile":
                pisitools.dosed(os.path.join(root, name), "pardusCC", get.CC())
                pisitools.dosed(os.path.join(root, name), "pardusCFLAGS", get.CFLAGS())

def setup():
    fixflags("./")

def build():
    shelltools.export("", get.CFLAGS())

    autotools.make('RPM_OPT_FLAGS="%(cflags)s" \
                    RPM_BUILD_ROOT="%(target)s" \
                    ROOT="%(target)s"' % D)

    shelltools.cd("irsockets")
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")

    autotools.install('PREFIX="%(target)s" \
                       ROOT="%(target)s" \
                       RPM_OPT_FLAGS="%(cflags)s" \
                       MANDIR="%(target)s/usr/share/man"' % D)

    pisitools.dodoc("README")
    pisitools.dodoc("etc/modules.conf.irda")
    pisitools.insinto(D["docdir"], "irsockets", "examples")

    # install README's into /usr/share/doc
    for i in ["irattach", "irdadump", "irdaping", "irsockets", "tekram"]:
        pisitools.newdoc(i + "/README", "README." + i)

    for i in ["irattach", "irdadump"]:
        pisitools.newdoc(i + "/ChangeLog", "ChangeLog." + i)

