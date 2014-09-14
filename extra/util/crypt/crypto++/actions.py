#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."
datadir = "/usr/share/%s" % get.srcNAME()

def setup():
    #delete GNUmakefile as it's not necessary anymore and messing things up if it's there
    shelltools.unlink("%s/GNUmakefile" % get.workDIR())

    #convert the DOS line endings of data files to unix type
    shelltools.system("dos2unix %s/License.txt" % get.workDIR())
    shelltools.system("dos2unix %s/Readme.txt" % get.workDIR())

    #create the configure script and configure to create only dynamic library
    for f in ["NEWS", "README", "AUTHORS", "ChangeLog"]:
        shelltools.touch(f)

    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static")

    pisitools.dosed("cryptopp.pc", "@VERSION@", get.srcVERSION())

def build():
    autotools.make()

def check():
    shelltools.system("./cryptestcwd v")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/pkgconfig", "cryptopp.pc")

    #cryptest* requires TestData files in cwd and they're just testing applications, not needed
    pisitools.remove("/usr/bin/cryptest*")
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("Readme*", "License*")
