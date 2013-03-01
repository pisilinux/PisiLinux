#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % (get.installDIR()))
    
    pisitools.dosym("/usr/bin/wodim", "usr/bin/cdrecord")
    pisitools.dosym("/usr/bin/readom", "usr/bin/readcd")
    pisitools.dosym("/usr/bin/genisoimage", "usr/bin/mkisofs")  
    pisitools.dosym("/usr/bin/genisoimage", "usr/bin/mkhybrid")    
    pisitools.dosym("/usr/bin/icedax", "usr/bin/cdda2wav")
    
    pisitools.dosym("/usr/share/man/man1/wodim.1", "usr/share/man/man1/cdrecord.1")
    pisitools.dosym("/usr/share/man/man1/readom.1", "usr/share/man/man1/readcd.1")
    pisitools.dosym("/usr/share/man/man1/genisoimage.1", "usr/share/man/man1/mkisofs.1")
    pisitools.dosym("/usr/share/man/man1/genisoimage.1", "usr/share/man/man1/mkhybrid.1")
    pisitools.dosym("/usr/share/man/man1/icedax.1", "usr/share/man/man1/cdda2wav.1")
    
    pisitools.dodoc("ABOUT", "Changelog", "COPYING", "FAQ", "FORK", "START", "TODO", "VERSION")
