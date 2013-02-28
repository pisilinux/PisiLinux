#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--enable-gui \
                         --enable-wxwidgets \
                         --enable-lzo \
                         --enable-bz2 \
                         --with-flac \
                         --disable-qt4")

def build():
    autotools.make('STRIP="true"')

def install():
    autotools.rawInstall('DESTDIR="%s" STRIP="true"' % get.installDIR())

    for f in ["examples", "doc/mkvmerge-gui.html", "doc/images"]:
        if shelltools.isFile(f) or shelltools.isDirectory(f):
            pisitools.insinto(docdir, f)

    # pisitools.insinto("/usr/share/pixmaps", "src/mmg/matroskalogo_big.xpm", "mmg.xpm")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
