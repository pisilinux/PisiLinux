#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

shelltools.export("CXXFLAGS", "%s -fno-strict-aliasing -DBIG_JOINS=1 -felide-constructors -fno-rtti" % get.CFLAGS())
shelltools.export("CFLAGS", "%s -fno-strict-aliasing -DBIG_JOINS=1 -fomit-frame-pointer" % get.CFLAGS())

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSYSCONFDIR=/etc/mysql \
    -DMYSQL_DATADIR=/var/lib/mysql \
    -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock \
    -DDEFAULT_CHARSET=utf8 \
    -DDEFAULT_COLLATION=utf8_general_ci \
    -DENABLED_LOCAL_INFILE=ON \
    -DINSTALL_INFODIR=share/mysql/docs \
    -DINSTALL_MANDIR=share/man \
    -DINSTALL_PLUGINDIR=lib/mysql/plugin \
    -DINSTALL_SCRIPTDIR=bin \
    -DINSTALL_INCLUDEDIR=include/mysql \
    -DINSTALL_DOCREADMEDIR=share/mysql \
    -DINSTALL_SUPPORTFILESDIR=share/mysql \
    -DINSTALL_MYSQLSHAREDIR=share/mysql \
    -DINSTALL_DOCDIR=share/mysql/docs \
    -DINSTALL_SHAREDIR=share/mysql \
    -DWITH_READLINE=ON \
    -DWITH_ZLIB=system \
    -DWITH_SSL=system \
    -DWITH_LIBWRAP=OFF \
    -DWITH_EXTRA_CHARSETS=complex \
    -DWITH_EMBEDDED_SERVER=ON \
    -DWITH_ARCHIVE_STORAGE_ENGINE=1 \
    -DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DWITH_PARTITION_STORAGE_ENGINE=1 \
    -DWITH_TOKUDB_STORAGE_ENGINE=1 \
    -DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 \
    -DWITHOUT_FEDERATED_STORAGE_ENGINE=1 \
    -DWITHOUT_PBXT_STORAGE_ENGINE=1")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.install("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Config
    pisitools.insinto("/etc/mysql", "%s/usr/share/mysql/my-medium.cnf" % get.installDIR(), "my.cnf")
    pisitools.insinto("/etc/mysql", "%s/%s/scripts/mysqlaccess.conf" % (get.workDIR(), get.srcDIR()))

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Runtime data
    pisitools.dodir("/run/mysqld")
    # Documents
    pisitools.dodoc("%s/%s/support-files/my-*.cnf" % (get.workDIR(), get.srcDIR()))
    pisitools.dodoc("COPYING", "INSTALL-SOURCE", "README", "VERSION")
