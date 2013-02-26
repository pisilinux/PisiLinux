# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():
    shelltools.system("./buildconf")

    # Some php extensions attempt to connect to X server. Ignore php
    # configuration to disable all extensions during the build.
    pisitools.dosed("configure", r"(\$PHP --version)", r"\1 --no-php-ini")

    autotools.configure("--enable-php-gtk \
                         --disable-debug \
                         --disable-gtktest \
                         --enable-scintilla \
                         --enable-shared \
                         --disable-static \
                         --with-extra \
                         --with-html \
                         --with-libglade \
                         --with-libsexy \
                         --with-mozembed \
                         --without-sourceview \
                         --with-spell")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)

def build():
    autotools.make("PHP='/usr/bin/php --no-php-ini'")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dosym("../../ext/60-php-gtk.ini", "/etc/php/cli/ext/60-php-gtk.ini")
    pisitools.dodoc("AUTHORS", "COPYING.LIB", "NEWS", "README*", "TODO2")
