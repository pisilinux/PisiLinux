#!/usr/bin/python
# * coding: utf8 *
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s fPIC fnostrictaliasing" % get.CFLAGS())

 def setup():
    autotools.aclocal("I m4")
    autotools.autoheader()
    libtools.libtoolize()
    shelltools.system("intltoolize force copy automake")
    autotools.autoreconf("fi") 
    autotools.configure("disablestatic \
                         libexecdir=/usr/lib/evolutiondataserver \
                         enablevalabindings \
                         disableuoa")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")