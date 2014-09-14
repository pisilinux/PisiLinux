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
    #shelltools.export("CFLAGS","%s -fPIE" % get.CFLAGS())
    #shelltools.export("LDFLAGS", "%s -pie -Wl,-z,relro,-z,now"  % get.LDFLAGS())

    autotools.configure("--enable-symcryptrun \
                         --disable-rpath \
                         --enable-gpgtar \
                         --enable-maintainer-mode")

def build():
    autotools.make("-j1")
    autotools.make("-C doc html")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s libexecdir="/usr/libexec"' % get.installDIR())

    # Compat symlinks
    pisitools.dosym("gpg2", "/usr/bin/gpg")
    pisitools.dosym("gpgv2", "/usr/bin/gpgv")
    pisitools.dosym("gpg2.1", "/usr/share/man/man1/gpg.1")
    pisitools.dosym("gpgv2.1", "/usr/share/man/man1/gpgv.1")

    # Lets make doc
    pisitools.dohtml("doc/*")
    pisitools.dohtml("doc/gnupg.html/*")
    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
