# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s.%s" % (get.srcNAME(), get.srcVERSION(), get.ARCH())

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "usr/lib/*")
        return
    else:
        pisitools.insinto("/usr/lib", "usr/lib/*")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
