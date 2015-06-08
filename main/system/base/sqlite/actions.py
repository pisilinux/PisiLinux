#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

    # Use secure delete. Even if the data is deleted with sqlite query, the traces of the deleted data still remains in the file
    # but cannot be seen with sqlite query. However, it can be seen by opening the file with a text editor.
    # SQLITE_SECURE_DELETE overwrites written data with zeros.
def setup():
    pisitools.cflags.add("-DSQLITE_SECURE_DELETE",
                         "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
                         "-DSQLITE_ENABLE_COLUMN_METADATA",
                         "-DSQLITE_DISABLE_DIRSYNC",
                         "-DSQLITE_ENABLE_FTS3",
                         "-DSQLITE_ENABLE_FTS4",
                         "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
                         "-DSQLITE_ENABLE_STMT_SCANSTATUS",
                         "-DSQLITE_SOUNDEX",
                         "-DSQLITE_ENABLE_RTREE",
                         "-DSQLITE_ENABLE_API_ARMOR")
    
    pisitools.cflags.sub("-O[s\d]", "-O3")
    
    autotools.configure("--disable-static \
                         --enable-readline \
                         --enable-threadsafe")
    
    shelltools.cd("tea")
    autotools.configure(" \
                         --enable-shared \
                         --with-tcl='/usr/lib/' \
                         --with-tclinclude='/usr/include' \
                         --enable-64bit \
                         --enable-threads")
    
def build():
    autotools.make("-j1")
    
    shelltools.cd("tea")
    autotools.make("-j1")
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("%s/sqlite-autoconf-3081002/tea" % get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
    
    shelltools.cd("%s/sqlite-doc-3081002" % get.workDIR())
    shelltools.system("pwd")
    
    pisitools.insinto("/usr/share/doc/sqlite", "../sqlite-doc-3081002/*")
    
    # fix permissions and remove obsolete files; https://bugs.archlinux.org/task/24605
    shelltools.system("find %s -type f -perm 755 -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -type f -perm 755 -exec chmod 644 {} \;" % get.installDIR())
    shelltools.system("find %s -type f -name '*~' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -type d -name '*~' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -name '*~' -exec rm -f {} \;" % get.installDIR())
    shelltools.system("find %s -type f -name '.~*' -exec ls -lha {} \;" % get.installDIR())# /build/pkg/sqlite-doc/usr/share/doc/sqlite/images/fileformat/.~lock.indexpage.odg#
    shelltools.system("find %s -type d -name '.~*' -exec ls -lha {} \;" % get.installDIR())
    shelltools.system("find %s -name '.~*' -exec rm -f {} \;" % get.installDIR())