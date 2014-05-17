#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

pisitools.flags.add("-fPIC -fno-strict-aliasing -fno-strict-overflow -fstack-protector-all")
pisitools.cxxflags.add("-I/usr/include/et")

def rename_man_pages():
    manpages = ["appl/bsd/klogind.M",
                "appl/bsd/kshd.M",
                "appl/sample/sserver/sserver.M",
                "appl/telnet/telnetd/telnetd.8",
                "appl/gssftp/ftpd/ftpd.M",
                "config-files/kdc.conf.M",
                "config-files/krb5.conf.M",
                "kadmin/cli/kadmin.M",
                "slave/kpropd.M",
                "slave/kprop.M"]
    for manpage in manpages:
        shelltools.move(manpage, "%s.in" % manpage)

def setup():
    shelltools.cd("src")
    shelltools.system("sed -i -e 's/^YYSTYPE yylval/&={0}/' lib/krb5/krb/deltat.c")
    pisitools.dosed("util/ac_check_krb5.m4", "(KRB5ROOT=\/usr)\/local", r"\1")

    autotools.autoreconf("-fi")

    # Fix pthread linking
    #pisitools.dosed("configure", "-lthread", "-lpthread")
    #pisitools.dosed("configure", "-pthread", "-lpthread")

    autotools.configure("--localstatedir=/var/lib \
                         --without-tcl \
                         --without-hesiod \
                         --enable-shared \
                         --enable-kdc-lookaside-cache \
                         --without-system-verto \
                         --disable-rpath \
                         --with-system-et \
                         --with-system-ss \
                         --enable-dns-for-realm")

    # Fix krb5-config script to remove rpaths and CFLAGS
    #pisitools.dosed("krb5-config", "^CC_LINK=.*", "CC_LINK='$(CC) $(PROG_LIBPATH)'")
    # Fix unused dependency
    pisitools.dosed("config/shlib.conf"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-C src/")

def check():
    autotools.make("-C src/ -j1 check")
   # import tempfile
   # import shutil
   # tmpdir = tempfile.mkdtemp(prefix='pisitest')
   # autotools.make("-C src/ check TMPDIR=%s -j1" % tmpdir)
   # shutil.rmtree("rm -rf %s" % tmpdir)

def install():
    pisitools.dodoc("NOTICE", "README")
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install additional headers
    for d in ("kadm5", "krb5"):
        pisitools.insinto("/usr/include/%s" % d, "include/%s/*.h" % d)

    # Add "k" prefix to some apps and manpages to resolve conflicts
    #for app in ["telnetd", "ftpd"]:
     #   pisitools.rename("/usr/share/man/man8/%s.8" % app, "k%s.8" % app)
      #  pisitools.rename("/usr/sbin/%s" % app, "k%s" % app)

    #for app in ["rcp", "rsh", "telnet", "ftp", "rlogin"]:
     #   pisitools.rename("/usr/share/man/man1/%s.1" % app, "k%s.1" % app)
      #  pisitools.rename("/usr/bin/%s" % app, "k%s" % app)

    # Remove examples
    pisitools.removeDir("/usr/share/examples")
