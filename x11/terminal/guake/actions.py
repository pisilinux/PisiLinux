#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    #fix running autogen.sh  
    shelltools.system('sed -i "/AM_INIT_AUTOMAKE/ s/-Werror//" configure.ac')
    shelltools.system("./autogen.sh")
    
    autotools.configure("--disable-static --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/pixmaps/guake/guake.png", "/usr/share/pixmaps/guake.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
