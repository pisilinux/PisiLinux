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
    pisitools.dosed("etc/faxsetup.sh.in", "ALIASES=/usr/lib/aliases", "ALIASES=/etc/mail/aliases")
    autotools.rawConfigure("--nointeractive \
                            --with-DIR_BIN=/usr/bin \
                            --with-DIR_SBIN=/usr/sbin \
                            --with-DIR_LIB=/usr/lib \
                            --with-DIR_LIBEXEC=/usr/sbin \
                            --with-DIR_LIBDATA=/usr/lib/fax \
                            --with-DIR_LOCALE=/usr/share/locale \
                            --with-DIR_LOCKS=/var/lock \
                            --with-DIR_MAN=/usr/share/man \
                            --with-DIR_SPOOL=/var/spool/fax \
                            --with-FAXGID=dialout \
                            --with-FAXUID=dialout \
                            --with-DIR_HTML=/usr/share/doc/%s/html \
                            --with-DIR_CGI=%s \
                            --with-HTML=yes \
                            --with-PATH_DPSRIP=/var/spool/fax/bin/ps2fax \
                            --with-PATH_IMPRIP=\"\" \
                            --with-SYSVINIT=no \
                            --with-FONTMAP=/usr/share/fonts/default/ghostscript \
                            --with-LIBTIFF=\"-ltiff -ljpeg -lz\" \
                            --with-OPTIMIZER=\"%s\" \
                            --with-DSO=auto \
                            --with-REGEX=yes \
                            --with-PATH_EGETTY=/bin/false \
                            --with-PATH_VGETTY=/bin/false \
                            --with-PAGESIZE=A4" % (get.srcNAME(), get.curDIR(), get.CFLAGS()))

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/usr/lib/fax")
    pisitools.dodir("/usr/share/man")
    pisitools.dodir("/usr/share/locale")
    pisitools.dodir("/var/spool")
    pisitools.dodir("/var/spool/recvq")
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())

    autotools.rawInstall("BIN=%(INSTALL)s/usr/bin \
                          SBIN=%(INSTALL)s/usr/sbin \
                          LIBDIR=%(INSTALL)s/usr/lib \
                          LIB=%(INSTALL)s/usr/lib \
                          LIBEXEC=%(INSTALL)s/usr/sbin \
                          LIBDATA=%(INSTALL)s/usr/lib/fax \
                          LOCALEDIR=%(INSTALL)s/usr/share/locale \
                          MAN=%(INSTALL)s/usr/share/man \
                          SPOOL=%(INSTALL)s/var/spool/fax \
                          HTMLDIR=%(INSTALL)s/usr/share/doc/%(DOC)s/html" % {'INSTALL':get.installDIR(), 'DOC':get.srcNAME()})

    pisitools.dodoc("doc/*", "CONTRIBUTORS", "COPYRIGHT", "README", "TODO")