#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    #libtools.libtoolize("--force --copy")

    # May have trouble with cpu flags
    autotools.configure("--with-x \
                         --enable-libxmi \
                         --enable-libplotter \
                         --enable-ps-fonts-in-pcl \
                         --enable-static=no")
    
    # fix rpath handling
    shelltools.system("sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool")
    shelltools.system("sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool")

def build():
    autotools.make()

def install():
    autotools.install("datadir=%s/usr/share" % get.installDIR())

    # these files are too generic named and they conflict with other packages like cel
    for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.rename("/usr/bin/%s" % f, "plotutils-%s" % f)

    pisitools.dodoc("AUTHORS", "COMPAT", "ChangeLog", "KNOWN_BUGS", "NEWS", "ONEWS", "PROBLEMS", "README", "THANKS", "TODO")

    # FIXME: we are not installing the ps fonts now, we should check if it breaks ghostscript and printers
    # read INSTALL.fonts for more info
