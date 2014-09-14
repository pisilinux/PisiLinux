#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

cflags = "-DUTF8=1 -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE %s -fgnu89-inline -I/usr/include/gssapi" % get.CFLAGS()

def setup():
    shelltools.export("CFLAGS", cflags)
    #shelltools.move("po/no.po",  "po/nb.po")
    # shelltools.move("po/no.gmo", "po/nb.gmo")
    # shelltools.unlink("po/tr.gmo")

    # Make sure we don't need cvs for autopoint
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--with-screen=slang \
                         --with-gpm-mouse \
                         --with-vfs \
                         --with-ext2undel \
                         --with-edit \
                         --with-x=yes \
                         --enable-charset \
                         --enable-nls \
                         --with-samba \
                         --with-configdir=/etc/samba \
                         --with-codepagedir=/var/lib/samba/codepages \
                         --with-privatedir=/etc/samba/private")
                         # --with-included-gettext \

def build():
    shelltools.export("CFLAGS", cflags)
    autotools.make()

    shelltools.cd("po")
    autotools.make("tr.gmo")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ABOUT*", "AUTHORS", "ChangeLog", "NEWS", "README*")

    # Do not mess with glibc files
    # pisitools.remove("/usr/share/locale/locale.alias")

    # Do not carry empty dirs
    #pisitools.removeDir("/usr/sbin")
    #pisitools.removeDir("/usr/share/man/man8")
    #pisitools.removeDir("/usr/share/man/sr/man8")
