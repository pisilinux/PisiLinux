#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
	cmaketools.configure()


def build():
    cmaketools.make()

def install():
	cmaketools.install("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("README")
	#Needed by APBS plugin of PyMOL
	shelltools.chmod("tools/manip/psize.py", 0755)
	pisitools.insinto("/usr/bin", "tools/manip/psize.py", "psize")
	
	##create freemol directory and symlink, some programs (like pymol) may look here to source python file directly
	pydir = "/usr/lib/%s/site-packages/" % get.curPYTHON()
	pisitools.dodir("%s/pymol/freemol/bin" % pydir)
	
	pisitools.dosym("/usr/bin/psize", "%s/pymol/freemol/bin/psize.py" % pydir)