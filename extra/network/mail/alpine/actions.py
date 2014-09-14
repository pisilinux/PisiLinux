#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    #as-needed fix from Gentoo
    pisitools.dosed("alpine/Makefile.in", "@LIBS@$", "@LIBS@ -lpam -lkrb5")

    autotools.configure("--disable-static \
                         --enable-from-encoding \
                         --without-tcl \
                         --with-ssl-dir=/usr/lib \
                         --with-ssl-certs-dir=/etc/ssl/certs \
                         --with-c-client-target=lfd \
                         --with-debug-files=2 \
                         --with-debug-file=.alpine.debug \
                         --with-simple-spellcheck=hunspell \
                         --with-interactive-spellcheck=hunspell \
                         --with-system-pinerc=/%s/alpine.conf \
                         --with-system-fixed-pinerc=/%s/alpine.conf.fixed"% (get.confDIR(), get.confDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("imap/mailutil/mailutil")
    pisitools.dosbin("imap/mlock/mlock")

    pisitools.dohtml("doc/tech-notes/*.html")
    pisitools.dodoc("doc/tech-notes.txt", "NOTICE", "LICENSE", "README", "VERSION")
