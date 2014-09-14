#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--with-logdir=/var/log/dansguardian \
                         --with-piddir=/run \
                         --enable-clamav \
                         --enable-clamd \
                         --enable-icap \
                         --enable-kavd \
                         --enable-commandline \
                         --enable-trickledm \
                         --enable-ntlm \
                         --enable-email \
                         --with-proxyuser=dansguardian \
                         --with-proxygroup=dansguardian")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No useful, contains init scripts
    pisitools.removeDir("/usr/share/dansguardian/scripts")

    # Generates index.html, better to have x bit.
    shelltools.chmod("%s/usr/share/dansguardian/dansguardian.pl" % get.installDIR(), 0755)

    pisitools.dodir("/var/log/dansguardian")
