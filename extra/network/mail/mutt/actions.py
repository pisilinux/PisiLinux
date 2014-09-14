#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    #autotools.autoreconf()
    autotools.configure("--enable-smtp \
                         --enable-pop \
                         --enable-imap \
                         --enable-pgp \
                         --enable-hcache \
                         --enable-gpgme \
                         --without-idn \
                         --with-curses \
                         --with-regex \
                         --with-ssl \
                         --with-sasl \
                         --with-bdb \
                         --with-homespool=Maildir")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/etc/mime.types*")

    for pkg in ["flea", "muttbug"]:
        pisitools.remove("/usr/bin/%s" % pkg)
        pisitools.remove("/usr/share/man/man1/%s.1" % pkg)

    pisitools.insinto("/etc", "contrib/gpg.rc", "Muttrc.gpg.dist")

