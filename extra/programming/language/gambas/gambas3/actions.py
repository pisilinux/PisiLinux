# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Remove bundled font
    #shelltools.unlink("gb.sdl/src/data/*.ttf")
    shelltools.unlink("gb.sdl/src/data/LICENSE")

    # Remove the directory if empty
    if not shelltools.ls("gb.sdl/src/data"):
        shelltools.unlinkDir("gb.sdl/src/data")

    autotools.autoreconf("-vif")
    autotools.configure("--enable-bzlib2 \
                         --enable-zlib \
                         --enable-mysql \
                         --enable-odbc \
                         --enable-postgresql \
                         --disable-sqlite2 \
                         --enable-sqlite3 \
                         --enable-net \
                         --enable-curl \
                         --enable-smtp \
                         --enable-pcre \
                         --enable-sdl \
                         --enable-sdlsound \
                         --enable-xml \
                         --enable-v4l \
                         --enable-crypt \
                         --enable-qt4 \
                         --enable-gtk \
                         --enable-opengl \
                         --enable-desktop \
                         --enable-pdf \
                         --enable-cairo \
                         --enable-imageio \
                         --enable-imageimlib \
                         --enable-dbus \
                         --with-bzlib2-libraries=/lib")

def build():
    autotools.make()

def install():
    # Reset XDG_UTILS to avoid sandbox violations
    autotools.rawInstall("DESTDIR=%s XDG_UTILS=''" % get.installDIR())

    # See http://gambasdoc.org/help/howto/package#t2 for details.
    # These are temporary files used for generating gb.info and gb.list only.
    pisitools.remove("/usr/lib/gambas3/gb.[ls][ao]")
    pisitools.remove("/usr/lib/gambas3/gb.so.*")

    mimes = ("main/mime/application-x-gambas3",
             "app/mime/application-x-gambasscript",
             "app/mime/application-x-gambasserverpage")

    for mime in mimes:
        pisitools.insinto("/usr/share/mime/packages", "%s.xml" % mime)
        pisitools.insinto("/usr/share/icons/hicolor/64x64/mimetypes", "%s.png" % mime)

    for res in 16, 32:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (res, res), "comp/src/gb.form/stock/%s/gambas.png" % res, "gambas3.png")

    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "comp/src/gb.form/stock/scalable/gambas.svg", "gambas3.svg")

    pisitools.dodoc("COPYING", "README")
