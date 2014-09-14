#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob
import os

WorkDir = "lp_solve_5.5"

def setup():
    pisitools.dosed("lpsolve55/ccc", "^opts.*", "opts='%s'" % get.CFLAGS())
    pisitools.dosed("lp_solve/ccc", "^opts.*", "opts='%s'" % get.CFLAGS())

def build():
    shelltools.cd("lpsolve55")
    shelltools.system("sh -x ccc")

    shelltools.cd("../lp_solve")
    shelltools.system("sh -x ccc")

def install():
    pisitools.dobin("lp_solve/bin/ux*/lp_solve")

    for lib in glob.glob("lpsolve55/bin/ux*/*.so"):
        pisitools.dolib_so(lib)
        baselib = os.path.basename(lib)
        pisitools.domove("/usr/lib/%s" % baselib, "/usr/lib", baselib + ".0.0.0")
        pisitools.dosym("/usr/lib/%s.0.0.0" % baselib, "/usr/lib/%s" % baselib)
        pisitools.dosym("/usr/lib/%s.0.0.0" % baselib, "/usr/lib/%s" % baselib + ".0")

    pisitools.dodir("/usr/include/lpsolve")
    pisitools.insinto("/usr/include/lpsolve", "*.h")

    pisitools.dodoc("README.txt", "bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt", "bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt", "bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt")
