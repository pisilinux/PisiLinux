# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s.%s" % (get.srcNAME(), get.srcVERSION(), get.ARCH())

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "../%s-%s.i686/usr/lib/*" % (get.srcNAME(), get.srcVERSION()))
        return
    else:
        pisitools.insinto("/usr/lib", "usr/lib/*")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
