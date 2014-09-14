#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import texlivemodules

import os

WorkDir = "."

def setup():
    
    shelltools.makedirs("%s/source/build" % get.workDIR())
    shelltools.cd("%s/source/build" % get.workDIR())
    shelltools.sym("../configure", "configure")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --datarootdir=/usr/share \
                         --datadir=/usr/share \
                         --mandir=/usr/share/man \
                         --disable-native-texlive-build \
                         --with-banner-add=/PisiLinux \
                         --disable-multiplatform \
                         --disable-dialog \
                         --disable-psutils \
                         --disable-t1utils \
                         --disable-bibtexu \
                         --disable-xz \
                         --disable-web2c \
                         --enable-shared \
                         --disable-static \
                         --with-system-zlib \
                         --with-system-zziplib \
                         --with-system-pnglib \
                         --with-system-ncurses \
                         --with-system-t1lib \
                         --with-system-gd \
                         --with-system-poppler \
                         --with-system-xpdf \
                         --with-system-freetype2 \
                         --with-system-pixman \
                         --with-system-cairo \
                         --with-system-harfbuzz \
                         --with-system-graphite \
                         --with-system-icu \
                         --with-freetype2-libdir=/usr/lib \
                         --with-freetype2-include=/usr/include/freetype2 \
                         --with-xdvi-x-toolkit=xaw \
                         --disable-dump-share \
                         --disable-aleph \
                         --enable-luatex \
                         --with-clisp-runtime=default \
                         --enable-xindy \
                         --disable-xindy-rules \
                         --disable-xindy-docs ")

def build():
  
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.make()
 
def install():
        
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/tlpkg/TeXLive")
    shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())
    
    
    # install texmf tree
    folders = ["/usr/share",
	       "/etc/texmf/chktex",
	       "/etc/texmf/tex/",
               "/etc/texmf/web2c",
               "/etc/texmf/dvips/config",
               "/etc/texmf/dvipdfm",
               "/etc/texmf/texconfig",
               "/etc/texmf/ttf2pk",
               "/etc/texmf/xdvi",
               "/etc/fonts/conf.avail",
               "/etc/texmf/dvipdfmx"]

    for dirs in folders:
        pisitools.dodir(dirs)

    # remove aleph from fmtutil.cnf
    pisitools.dosed("%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), "^.*aleph.*$")
    
    pisitools.insinto("/etc/texmf/chktex", "%s/usr/share/texmf-dist/chktex/chktexrc" % get.installDIR(), sym=True) 
    pisitools.insinto("/etc/texmf/web2c", "%s/usr/share/texmf-dist/web2c/texmf.cnf" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/web2c", "%s/usr/share/texmf-dist/web2c/fmtutil.cnf" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/texconfig", "%s/usr/share/texmf-dist/texconfig/tcfmgr.map" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/dvipdfmx", "%s/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/ttf2pk", "%s/usr/share/texmf-dist/ttf2pk/ttf2pk.cfg" % get.installDIR(), sym=True)
    pisitools.insinto("/etc/texmf/xdvi", "%s/usr/share/texmf-dist/xdvi/XDvi" % get.installDIR(), sym=True)

    # fix symlinks, some are incorrect
    # makefile patching is another way, but there ar/dvipdfmx.cfge lot of scripts
    # pathing each makefile makes it much harder, for now this is a "simpler" solution
    for binary in shelltools.ls(get.installDIR() + "/usr/bin"):
        real_path = shelltools.realPath(get.installDIR() + "/usr/bin/" + binary)
        if "texmf" in real_path and not os.path.exists(real_path): # modify only if it is broken
            base_path = real_path.replace(get.installDIR() + "/usr", "")
            new_path = "/usr/share" + base_path
            shelltools.unlink(get.installDIR() + "/usr/bin/" + binary)
            pisitools.dosym(new_path, "/usr/bin/" + binary)

    # create symlinks for formats
    # shelltools.export("PATH", get.installDIR() + "/usr/bin")
    #shelltools.system("PATH=\"$PATH:%s/usr/bin\" texlinks -f %s/usr/share/texmf-dist/web2c/fmtutil.cnf %s/usr/bin/" % (get.installDIR(), get.installDIR(), get.installDIR()))

    # remove files form disabled packages
    # we copy all man and info files into mandir. Disabling packages just remove binaries.
    # the remaining man and info files should be deleted manually
    
    pisitools.remove("/usr/share/texmf-dist/fonts/map/dvipdfmx/cid-x.map")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/texglyphlist.txt")
    pisitools.remove("/usr/share/texmf-dist/scripts/chktex/chkweb.sh")
    pisitools.remove("/usr/share/texmf-dist/fonts/enc/dvips/base/7t.enc")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/pdfglyphlist.txt")
    pisitools.remove("/usr/share/texmf-dist/scripts/chktex/deweb.pl")
    pisitools.remove("/usr/share/texmf-dist/scripts/ps2eps/ps2eps.pl")
    pisitools.remove("/usr/share/texmf-dist/fonts/cmap/dvipdfmx/EUC-UCS2")
    pisitools.remove("/usr/share/texmf-dist/chktex/chktexrc")
    pisitools.remove("/usr/share/texmf-dist/dvipdfmx/dvipdfmx.cfg")
    pisitools.remove("/usr/share/texmf-dist/fonts/map/glyphlist/glyphlist.txt")

