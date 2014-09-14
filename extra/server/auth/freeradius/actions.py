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
    shelltools.export("CFLAGS", "%s -DLDAP_DEPRECATED -fPIC -DPIC" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie" % get.LDFLAGS())

    autotools.configure('--libdir=/usr/lib/freeradius \
                         --with-system-libtool \
                         --with-system-libltd \
                         --with-modules="rlm_wimax" \
                         --with-rlm-sql_postgresql-include-dir=/usr/include/pgsql \
                         --with-rlm-sql_postgresql-lib-dir=/usr/lib \
                         --with-rlm-sql_mysql-include-dir=/usr/include/mysql \
                         --with-rlm-sql_mysql-lib-dir=/usr/lib/mysql \
                         --with-unixodbc-lib-dir=/usr/lib \
                         --with-rlm-dbm-lib-dir=/usr/lib \
                         --with-rlm-krb5-include-dir=/usr/include/krb5 \
                         --with-modules="rlm_wimax" \
                         --with-rlm_eap_tls \
                         --with-rlm_eap_ttls \
                         --with-rlm_eap_peap \
                         --with-rlm_eap_otp \
                         --without-rlm_eap_ikev2 \
                         --without-rlm_sql_iodbc \
                         --without-rlm_sql_firebird \
                         --without-rlm_sql_db2 \
                         --without-rlm_sql_oracle \
                         --without-rlm_eap_tnc \
                         --without-rlm_unbound \
                         --enable-strict-dependencies \
                         --with-threads \
                         --with-threads-pool \
                         --with-edir \
                         --with-udp-fromto \
                         --with-pic \
                         --disable-static')

def build():
    shelltools.makedirs("build/lib/local")
    shelltools.makedirs("build/bin/local")
    autotools.make()

def install():
    autotools.rawInstall("R=%s" % get.installDIR())

    pisitools.dodir("/run/radiusd")
    pisitools.dodir("/var/lib/radiusd")
    pisitools.dodir("/var/log/radius/radacct")

    shelltools.touch("%s/var/log/radius/radutmp" % get.installDIR())
    shelltools.touch("%s/var/log/radius/radius.log" % get.installDIR())

    # remove useless files
    pisitools.remove("/usr/sbin/rc.radiusd")

    pisitools.remove("/etc/raddb/experimental.conf")

    #pisitools.insinto("/usr/share/doc/freeradius/", "scripts")

    pisitools.dosed("%s/etc/raddb/radiusd.conf" % get.installDIR(), '^#user *= *radius', 'user = radiusd')
    pisitools.dosed("%s/etc/raddb/radiusd.conf" % get.installDIR(), '^#group *= *radius', 'group = radiusd')

    pisitools.removeDir("/var/run/")

    pisitools.dodoc("CREDITS", "README*", "COPYRIGHT", "LICENSE")
