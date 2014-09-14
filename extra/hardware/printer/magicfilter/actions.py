#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "magicfilter-2.3.h"
conf = {"destdir": get.installDIR()}

def setup():
    shelltools.system("./configure.sh \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --filterdir=/usr/share/magicfilter/filters" % conf)

    pisitools.dosed("filters/*.def", "#! @MAGICFILTER@", "#!/usr/bin/magicfilter")
    pisitools.dosed("Makefile", "commoninstall: textonly cfmagic", "commoninstall: textonly")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%(destdir)s" % conf)

    pisitools.dodoc("README*", "Attic/COPYRIGHT")
