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
    pisitools.dosed("src/util/sys_defs.h", "hash:\/etc\/aliases", "hash:/etc/mail/aliases")

def build():
    cc_args = "-DHAS_PCRE -DHAS_MYSQL -I/usr/include/mysql -DHAS_PGSQL -I/usr/include/postgresql \
               -DUSE_TLS -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I/usr/include/sasl -DHAS_LDAP -fPIC"
    cc_libs = "-pie -Wl,-z,relro -Wl,-z,now -L/usr/lib -lpcre -lcrypt -lpthread -lpam -lssl -lcrypto -lsasl2 -lmysqlclient -lpq -lm -lz -lldap -llber"

    # Default paths
    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_README_DIR\s+\"no\"", \
                    "#define DEF_README_DIR \"/usr/share/doc/%s/readme\"" % get.srcNAME())

    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_HTML_DIR\s+\"no\"", \
                    "#define DEF_HTML_DIR \"/usr/share/doc/%s/html\"" % get.srcNAME())

    pisitools.dosed("src/global/mail_params.h", \
                    "#define DEF_MANPAGE_DIR\s+\"/usr/local/man\"", \
                    "#define DEF_MANPAGE_DIR \"/usr/share/man\"")

    pisitools.dosed("src/util/sys_defs.h", \
                    "#define NATIVE_DAEMON_DIR \"/usr/libexec/postfix\"", \
                    "#define NATIVE_DAEMON_DIR \"/usr/lib/postfix\"")

    autotools.make('CC=%s \
                    OPT="%s" \
                    CCARGS="%s" \
                    AUXLIBS="%s" makefiles' % (get.CC(), get.CFLAGS(), cc_args, cc_libs))

    autotools.make()

def install():
    shelltools.system('/bin/sh postfix-install \
                       -non-interactive \
                       install_root="%(installDIR)s" \
                       config_directory="/usr/share/doc/%(srcNAME)s/defaults" \
                       readme_directory="/usr/share/doc/%(srcNAME)s/readme" \
                       ' % {'installDIR': get.installDIR(), 'srcNAME': get.srcNAME()})

    pisitools.removeDir("/var/")

    # lets make dirs
    pisitools.dodir("/var/spool/postfix/")
    pisitools.dodir("/etc/mail/")
    pisitools.dodir("/etc/postfix/")
    pisitools.dodir("/var/spool/mail/")
    pisitools.dodir("/var/lib/postfix")
    pisitools.dosym("/var/spool/mail", "/var/mail")

    # qshape comes
    pisitools.dosbin("auxiliary/qshape/qshape.pl")
    pisitools.rename("/usr/sbin/qshape.pl", "qshape")

    # legacy FSH
    pisitools.dosym("/usr/sbin/sendmail", "/usr/lib/sendmail")

    # performance tuning tools.
    pisitools.dosbin("bin/smtp-source")
    pisitools.dosbin("bin/smtp-sink")
    pisitools.dosbin("bin/qmqp-source")
    pisitools.dosbin("bin/qmqp-sink")
    pisitools.doman("man/man1/smtp-source.1")
    pisitools.doman("man/man1/smtp-sink.1")
    pisitools.doman("man/man1/qmqp-source.1")
    pisitools.doman("man/man1/qmqp-sink.1")

    # Move some files
    pisitools.domove("/usr/share/doc/%s/defaults/master.cf" % get.srcNAME(), "/etc/postfix/")

    # Docs
    pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME(), "html/")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME(), "examples/")
    for s in ["*README", "COMPATIBILITY", "HISTORY", "LICENSE", "RELEASE_NOTES"]:
        pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME(), s)
