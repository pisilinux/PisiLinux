#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

pisitools.cflags.add("-fno-strict-aliasing", "-fPIC")

def setup():
    autotools.configure('--enable-svg \
                         --enable-pic \
                         --enable-ipv6 \
                         --enable-opengl \
                         --use-ft=system \
                         --use-js=no \
                         --use-a52=no \
                         --use-ffmpeg=system \
                         --use-ogg=system \
                         --use-vorbis=system \
                         --use-theora=system \
                         --use-faad=system \
                         --use-png=system \
                         --use-jpeg=system \
                         --use-mad=system \
                         --cc="%s" \
                         --extra-cflags="%s" \
                         --disable-wx \
                         --disable-amr \
                         --disable-oss-audio \
                         --disable-silent-rules \
                        ' % (get.CC(), get.CFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall('STRIP="true" DESTDIR="%s"' % get.installDIR())
    autotools.rawInstall('STRIP="true" DESTDIR="%s"' % get.installDIR(), "install-lib")

    pisitools.dosym("/usr/bin/MP4Box","/usr/bin/mp4box")
    pisitools.dosym("/usr/bin/MP4Client","/usr/bin/mp4client")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/*.txt")
    pisitools.dodoc("doc/*.doc")
    pisitools.doman("doc/man/*.1")

