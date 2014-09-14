#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("configure", "(virt_iodbc_dir\/include)", r"\1/iodbc")
    pisitools.dosed("configure", '(iodbc_CPPFLAGS=)"[^"]+"', r"\1`iodbc-config --cflags`")
    pisitools.dosed("configure", '(iodbc_LDFLAGS=)"[^"]+"', r"\1`iodbc-config --libs`")

    pisitools.dosed("configure", '\s+C[X]*FLAGS.*\$SED.*', deleteLine=True)

    autotools.configure("--localstatedir=/var \
                         --enable-shared \
                         --disable-static \
                         --without-internal-zlib \
                         --with-debug \
                         --with-iodbc \
                         --with-readline \
                         --disable-all-vads \
                         --disable-hslookup \
                         --enable-openssl \
                         --enable-xml")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")

def build():
    autotools.make()

"""
def check():
    #to fix thook.sh test this is required
    shelltools.export("HOST", "localhost")

    autotools.make("-j1 check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")

    #Rename generic filenames
    for f in ("inifile" ,"isql", "isqlw", "isql-iodbc", "isqlw-iodbc"):
        pisitools.domove("/usr/bin/%s" % f, "/usr/bin/", "virtuoso-%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "LICENSE", "NEWS", "README*")

    #remove duplicate documents
    pisitools.removeDir("/usr/share/virtuoso/doc")

    pisitools.dodir("/etc/virtuoso")
    pisitools.domove("/var/lib/virtuoso/db/virtuoso.ini", "/etc/virtuoso")
