#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("AR", "/usr/bin/ar")
    #shelltools.export("CC", "/usr/bin/cc")
    shelltools.export("RANLIB", "/usr/bin/ranlib")

    autotools.configure("--disable-multiplatform \
                         --enable-t1lib \
                         --enable-gf \
                         --disable-shared \
                         --with-system-t1lib \
                         --without-system-kpathsea \
                         --without-system-ptexenc \
                         --with-x-toolkit=xaw \
                         --enable-build-in-source-tree \
                         --with-xdvi-x-toolkit='motif'")
    
    
    
def build():
    autotools.make()
    shelltools.cd("texk/xdvik")
    shelltools.system("/usr/bin/emacs -batch -q --no-site-file -L  -f batch-byte-compile xdvi-search.el")

def install():
    pisitools.dodir("usr/texmf-dist/dvips/config/config.xdvi")
    pisitools.dodir("/etc/texmf/xdvi")
    pisitools.dodir("/etc/X11/app-defaults/")
    pisitools.dodir("/usr/share/texmf/xdvi/XDvi")

    shelltools.cd("texk/xdvik")

    autotools.install("texmf='%s/usr/share/texmf'" % get.installDIR())

    pisitools.domove("/usr/share/texmf/xdvi/XDvi" , "/usr/share/X11/app-defaults/")
    pisitools.dosym("/usr/share/X11/app-defaults/XDvi", "/usr/share/texmf/xdvi/XDvi")


    pisitools.insinto("/usr/share/emacs/site-lisp/tex-utils/", "*.el")

    pisitools.dodoc("BUGS", "FAQ", "README.*")
