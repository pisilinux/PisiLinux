 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get




def setup():
    autotools.configure("--prefix=install/usr \
                         --etcdir=install/etc \
                         --mandir=install/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.install()
    shelltools.move("install/*", "%s/" % get.installDIR())
    pisitools.domove("/axelrc", "/etc")
    shelltools.makedirs("%s/etc" % get.installDIR()) 
