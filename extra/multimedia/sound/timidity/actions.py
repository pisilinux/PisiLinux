#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "TiMidity++-%s" % get.srcVERSION()

def setup():
    audios = "flac,speex,vorbis,ao,alsa,jack"
    interfaces = "ncurses,vt100,alsaseq,server,network,gtk"

    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.autoconf()
    autotools.configure('--localstatedir=/var/state/timidity \
                         --with-elf \
                         --enable-audio="%s" \
                         --enable-interface="%s" \
                         --enable-server \
                         --enable-network \
                         --enable-dynamic \
                         --enable-vt100 \
                         --enable-spline=cubic \
                         --enable-slang \
                         --enable-ncurses \
                         --with-x \
                         --enable-spectrogram \
                         --enable-wrd \
                         --enable-xskin \
                         --enable-gtk \
                         --with-default-output=alsa \
                         --enable-alsaseq' % (audios, interfaces))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/etc/timidity.cfg", "/usr/share/timidity/timidity.cfg")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "doc/C/README*")
