#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    flags = "%s -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE \
                -fno-strict-aliasing -fwrapv \
                -fPIC" % get.CFLAGS()

    # remember this will soon be default in gcc
    if get.ARCH() == 'i686':
        flags += " -fno-omit-frame-pointer"

    # Export flags
    shelltools.export("CFLAGS", flags)
    shelltools.export("CXXFLAGS", "%s -felide-constructors -fno-rtti -fno-exceptions" % flags)

    # Configure!
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DSYSCONFDIR=/etc/mysql \
                          -DMYSQL_DATADIR=/var/lib/mysql \
                          -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock \
                          -DDEFAULT_CHARSET=utf8 \
                          -DDEFAULT_COLLATION=utf8_general_ci \
                          -DENABLED_LOCAL_INFILE=ON \
                          -DINSTALL_INFODIR=share/info \
                          -DINSTALL_MANDIR=share/man \
                          -DINSTALL_PLUGINDIR=lib/mysql/plugin \
                          -DINSTALL_SCRIPTDIR=bin \
                          -DINSTALL_SBINDIR=sbin \
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
                          -DWITH_EXTRA_CHARSETS=all \
                          -DWITH_EMBEDDED_SERVER=ON \
                          -DWITH_INNOBASE_STORAGE_ENGINE=1 \
                          -DWITH_PARTITION_STORAGE_ENGINE=1 \
                          -DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 \
                          -DWITHOUT_ARCHIVE_STORAGE_ENGINE=1 \
                          -DWITHOUT_BLACKHOLE_STORAGE_ENGINE=1 \
                          -DWITHOUT_FEDERATED_STORAGE_ENGINE=1 ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s benchdir_root=\"/usr/share/mysql\"" % get.installDIR())

    # Extra headers
    pisitools.insinto("/usr/include/mysql", "include/my_config.h")
    pisitools.insinto("/usr/include/mysql", "include/my_dir.h")

    # Links
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlanalyze")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqlrepair")
    pisitools.dosym("mysqlcheck", "/usr/bin/mysqloptimize")

    # Cleanup
    pisitools.remove("/usr/share/mysql/mysql.server")
    pisitools.remove("/usr/share/mysql/binary-configure")
    pisitools.remove("/usr/share/mysql/mysql-log-rotate")
    pisitools.remove("/usr/share/mysql/my-*.cnf")
    pisitools.remove("/usr/share/mysql/config.*")
    #pisitools.removeDir("/usr/share/aclocal")

    # Move libs to /usr/lib
    #pisitools.domove("/usr/lib/mysql/libmysqlclient*.so*", "/usr/lib")

    # Links to libs
    pisitools.dosym("../libmysqlclient.so", "/usr/lib/mysql/libmysqlclient.so")
    pisitools.dosym("../libmysqlclient_r.so", "/usr/lib/mysql/libmysqlclient_r.so")

    # No tests, benchs
    pisitools.removeDir("/usr/mysql-test")
    pisitools.removeDir("/usr/data")
    pisitools.removeDir("/usr/sql-bench")
    
    # Config
    pisitools.insinto("/etc/mysql", "scripts/mysqlaccess.conf")

    # Data dir
    pisitools.dodir("/var/lib/mysql")

    # Logs
    pisitools.dodir("/var/log/mysql")
    shelltools.touch("%s/var/log/mysql/mysql.log" % get.installDIR())
    shelltools.touch("%s/var/log/mysql/mysql.err" % get.installDIR())
    pisitools.dodir("/var/lib/mysql/innodb")

    # Runtime data
    pisitools.dodir("/run/mysqld")

    # Documents
    pisitools.dodoc("README", "COPYING")
    pisitools.dodoc("support-files/my-*.cnf")