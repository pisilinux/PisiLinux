#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

suffix = "32" if get.buildTYPE() == "emul32" else ""
bindir = "/tmp"  if get.buildTYPE() == "emul32" else "/bin"

def setup():
    autotools.rawConfigure("--libdir=/lib%s \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib%s \
                            --bindir=%s" % (suffix, suffix, bindir))
def build():
    autotools.make()

def install():
    autotools.make("DIST_ROOT=%s install install-lib install-dev" % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/tmp")
    pisitools.remove("/lib%s/libattr.a" % suffix)