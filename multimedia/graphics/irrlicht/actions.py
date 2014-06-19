#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

includedir = "/usr/include/irrlicht"
librarydir = "/usr/lib"
mainsrcdir = "source/Irrlicht"

srcversion = get.srcVERSION()
snapshotbuild = False

if "_pre" in srcversion:
    snapshotbuild = True
    abiversion = srcversion.rsplit("_pre", 1)[0].rsplit(".", 1)[0]
    srcversionname = "%s-SVN" % srcversion.rsplit("_pre", 1)[0]
else:
    abiversion = srcversion.rsplit(".", 1)[0]
    srcversionname = abiversion


def setup():
    shelltools.system("wget http://sourceforge.net/p/irrlicht/code/4600/tree/trunk/source/Irrlicht/COpenGLExtensionHandler.h?format=raw --output-document COpenGLExtensionHandler.h")
    shelltools.system("wget http://sourceforge.net/p/irrlicht/code/4600/tree/trunk/source/Irrlicht/glext.h?format=raw --output-document glext.h")
    shelltools.system("wget http://sourceforge.net/p/irrlicht/code/4600/tree/trunk/source/Irrlicht/glxext.h?format=raw --output-document glxext.h")
    shelltools.system("wget http://sourceforge.net/p/irrlicht/code/4600/tree/trunk/source/Irrlicht/wglext.h?format=raw --output-document wglext.h")
    
    for i in ["jpeglib", "zlib", "libpng"]:
        unwanteddir = "%s/%s" % (mainsrcdir, i)
        if shelltools.isDirectory(unwanteddir):
            shelltools.unlinkDir(unwanteddir)

    for i in ["include/*.h", "doc/upgrade-guide.txt", "%s/*.cpp" % mainsrcdir, "%s/*.h" % mainsrcdir]:
        pisitools.dosed(i, "\r")
        shelltools.chmod(i, 0644)

def build():
    shelltools.cd(mainsrcdir)
    autotools.make('sharedlib RPM_OPT_FLAGS="%s"' % get.CXXFLAGS() )

def install():
    autotools.rawInstall("-C %s INSTALL_DIR=%s/%s" % (mainsrcdir, get.installDIR(), librarydir))

    pisitools.dosym("/usr/lib/libIrrlicht.so.1.8.1", "/usr/lib/libIrrlicht.so.1")

    pisitools.dodoc("doc/*.txt", "*.txt")
    #pisitools.insinto("/usr/lib", "lib/Win32-gcc/libIrrlicht.a")

    if snapshotbuild:
        # snapshots need some touch for doc generation
       shelltools.cd("scripts/doc/irrlicht/")
       shelltools.system("./makedocumentation.sh")
       pisitools.dohtml("../../../doctemp/html/*")
    else:
       pisitools.dohtml("doc/html/*")