#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.dosed("avidemux/gtk/ADM_userInterfaces/ui_support.cpp",
                    '(#include\s"DIA_uiTypes\.h")',
                    r'\1\n#include "ADM_default.h"')
    shelltools.system("bash ./bootStrap.bash --with-cli --with-gtk --debug")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/", "install/usr")
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")
    pisitools.domo("po/ca.po", "ca", "avidemux.mo")
    pisitools.domo("po/cs.po", "cs", "avidemux.mo")
    pisitools.domo("po/de.po", "de", "avidemux.mo")
    pisitools.domo("po/el.po", "el", "avidemux.mo")
    pisitools.domo("po/es.po", "es", "avidemux.mo")
    pisitools.domo("po/fr.po", "fr", "avidemux.mo")
    pisitools.domo("po/it.po", "it", "avidemux.mo")
    pisitools.domo("po/ja.po", "ja", "avidemux.mo")
    pisitools.domo("po/pt_BR.po", "pt_BR", "avidemux.mo")
    pisitools.domo("po/ru.po", "ru", "avidemux.mo")
    pisitools.domo("po/sr.po", "sr", "avidemux.mo")
    pisitools.domo("po/sr@latin.po", "sr@latin", "avidemux.mo")
    pisitools.domo("po/tr.po", "tr", "avidemux.mo")

    pisitools.dodoc("COPYING", "AUTHORS", "License*")
    pisitools.doman("man/*")