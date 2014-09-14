#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/usr/share/fpcsrc"]

version = get.srcVERSION().split("_")[0]
sourceDir = "%s/%s" % (get.workDIR(), get.srcDIR())
ppc = "ppcx64" if get.ARCH() == "x86_64" else "ppc386"


def build():
    # Use the bootstrap compiler
    autotools.make("PP=%s/fpc-bootstrap/%s compiler_cycle" % (get.workDIR(), ppc))

    # Rebuild compiler using the new compiler
    shelltools.copy("compiler/%s" % ppc, "ppc_new")
    autotools.make("PP=%s/ppc_new compiler_cycle" % sourceDir)
    shelltools.unlink("ppc_new")
    shelltools.copy("compiler/%s" % ppc, "ppc_new")

    autotools.make("PP=%s/ppc_new all" % sourceDir)

def install():
    autotools.rawInstall("PP=%s/ppc_new INSTALL_PREFIX=%s/usr" % (sourceDir, get.installDIR()))
    pisitools.dosym("../lib/fpc/%s/%s" % (version, ppc), "/usr/bin/%s" % ppc)
    pisitools.removeDir("/usr/lib/fpc/lexyacc")

    shelltools.system("%(root)s/usr/lib/fpc/%(ver)s/samplecfg"
                      " %(root)s/usr/lib/fpc/%(ver)s %(root)s/etc" \
                        % {"root": get.installDIR(), "ver": version})

    autotools.make("PP=%s/ppc_new clean" % sourceDir)
    shelltools.copytree(".", "%s/usr/share/fpcsrc/" % get.installDIR())
    pisitools.remove("/usr/share/fpcsrc/ppc*")

    pisitools.rename("/usr/share/doc/fpc-%s" % version, get.srcNAME())
    pisitools.dodoc("compiler/COPYING*")
