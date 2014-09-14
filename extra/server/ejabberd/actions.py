#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    autotools.configure("--enable-pam \
                         --enable-odbc")

def build():
    autotools.make("-C src -j1")

def install():
    autotools.rawInstall("-C src DESTDIR=%s" % get.installDIR())

    # fix example SSL certificate path to real one,
    # which we created recently
    pisitools.dosed("%s/etc/ejabberd/ejabberd.cfg" % get.installDIR(),
                    "/path/to/ssl.pem",
                    "/etc/ejabberd/ejabberd.pem")

    # fix captcha path
    pisitools.dosed("%s/etc/ejabberd/ejabberd.cfg" % get.installDIR(),
                    "/lib/ejabberd/priv/bin/captcha.sh",
                    "/usr/lib/ejabberd/priv/bin/captcha.sh")

    pisitools.dodir("/var/lib/ejabberd/spool")
    pisitools.dodir("/var/lib/ejabberd/db")
    pisitools.dodir("/var/log/ejabberd")
    pisitools.dodir("/etc/ejabberd")

    # install sql-scripts for creating db schemes for various RDBMS
    pisitools.insinto("/usr/share/%s" % get.srcNAME(), "src/odbc/mssql*")
    pisitools.insinto("/usr/share/%s" % get.srcNAME(), "src/odbc/pg.sql")
    pisitools.insinto("/usr/share/%s" % get.srcNAME(), "src/odbc/mysql.sql")

    pisitools.dodoc("README", "COPYING")
