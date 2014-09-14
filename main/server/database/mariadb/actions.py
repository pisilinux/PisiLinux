#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

pisitools.flags.add("-fPIC -fno-strict-aliasing -DBIG_JOINS=1")
pisitools.cflags.add("-fomit-frame-pointer")
pisitools.cxxflags.add("-felide-constructors -fno-rtti")

def setup():
    pisitools.dosed("storage/tokudb/ft-index/ft/ft-ops.cc", "LEAFENTRY leaf_entry;", "LEAFENTRY leaf_entry = 0;")
    cmaketools.configure("-DBUILD_CONFIG=mysql_release \
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
                          -DWITHOUT_PBXT_STORAGE_ENGINE=1 \
                          -DWITHOUT_TOKUDB=1 \
                         ")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Config
    pisitools.insinto("/etc/mysql", "%s/usr/share/mysql/my-medium.cnf" % get.installDIR(), "my.cnf")
    pisitools.insinto("/etc/mysql", "%s/%s/scripts/mysqlaccess.conf" % (get.workDIR(), get.srcDIR()))

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Documents
    pisitools.dodoc("%s/%s/support-files/my-*.cnf" % (get.workDIR(), get.srcDIR()))
    pisitools.dodoc("COPYING", "INSTALL-SOURCE", "README", "VERSION")

    # Remove not needed files
    pisitools.removeDir("/usr/data")
    pisitools.removeDir("/usr/mysql-test")
    pisitools.removeDir("/usr/sql-bench")
    pisitools.remove("/usr/share/man/man1/mysql-test-run.pl.1")

    # Remove -lprobes_mysql
    pisitools.dosed("%s/usr/bin/mysql_config" % get.installDIR(), "-lprobes_mysql")
