#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("CFLAGS", "%s -Wa,--noexecstack" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -Wl,-z,noexecstack" % get.LDFLAGS())

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --fsstnd=PisiLinux \
                            --hyperspec=http://www.lispworks.com/documentation/HyperSpec/ \
                            --with-dynamic-ffi \
                            --with-module=bindings/glibc \
                            --with-module=clx/new-clx \
                            --with-module=dbus \
                            --with-module=fastcgi \
                            --with-module=gdbm \
                            --with-module=gtk2 \
                            --with-module=i18n \
                            --with-module=pcre \
                            --with-module=postgresql \
                            --with-module=rawsock \
                            --with-module=readline \
                            --with-module=regexp \
                            --with-module=syscalls \
                            --with-module=wildcard \
                            --with-module=zlib")
def build():
    autotools.make("-C src -j1")

def install():
    shelltools.cd("src")
    autotools.make("-j1 DESTDIR=%s prefix=/usr install-bin" % (get.installDIR()))

    shelltools.chmod("%s/usr/bin/clisp-link" % get.installDIR(), 0755)

    shelltools.cd("..")
    pisitools.dohtml("doc/impnotes.css","doc/impnotes.html","doc/_clisp.html","doc/clisp.png")
    pisitools.dodoc("doc/Symbol-Table.text","doc/CLOS-guide.txt","doc/LISP-tutorial.txt")

    pisitools.doman("doc/_clisp.1")
    pisitools.rename("/usr/share/man/man1/_clisp.1", "clisp.1")
