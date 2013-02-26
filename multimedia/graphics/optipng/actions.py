#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("src/scripts/gcc.mak.in", "prefix=/usr/local", "prefix=/usr")

    # Bad workaround to make use of internal png header
    #shelltools.copy("lib/libpng/pngpriv.h", "src/")

    #Ensure using system libraries
    #shelltools.unlinkDir("lib/libpng")
    #shelltools.unlinkDir("lib/zlib")

    autotools.rawConfigure("--with-system-zlib \
                         --with-system-libpng")

def build():
    # define PNG_USER_PRIVATEBUILD to pass ifdef check in opngreduc.c file
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("usr/local/bin/optipng", "/usr/bin/")
    pisitools.domove("usr/local/man/man1/optipng.1", "/usr/share/man/man1/")
    pisitools.removeDir("usr/local/")
    #pisitools.dobin("src/optipng")

    #pisitools.doman("man/optipng.1")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("LICENSE.txt", "README.txt", "doc/history.txt", "doc/todo.txt")
