#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./install.sh")

def install():
    pisitools.domo("po/de.po","de","isowriter.mo")

    pisitools.dobin("imagewriter")

    pisitools.dodoc("COPYING","TODO")

    pisitools.dolib("lib/*","/usr/lib/isowriter/")
    pisitools.domo("po/ar.po", "ar", "usb-imagewriter.mo")
    pisitools.domo("po/bg.po", "bg", "usb-imagewriter.mo")
    pisitools.domo("po/ca.po", "po", "usb-imagewriter.mo")
    pisitools.domo("po/cs.po", "cs", "usb-imagewriter.mo")
    pisitools.domo("po/da.po", "da", "usb-imagewriter.mo")
    pisitools.domo("po/de.po", "de", "usb-imagewriter.mo")
    pisitools.domo("po/el.po", "el", "usb-imagewriter.mo")
    pisitools.domo("po/en_CA.po", "en_CA", "usb-imagewriter.mo")
    pisitools.domo("po/en_GB.po", "en_GB", "usb-imagewriter.mo")
    pisitools.domo("po/es.po", "es", "usb-imagewriter.mo")
    pisitools.domo("po/fr.po", "fr", "usb-imagewriter.mo")
    pisitools.domo("po/he.po", "he", "usb-imagewriter.mo")
    pisitools.domo("po/hu.po", "hu", "usb-imagewriter.mo")
    pisitools.domo("po/id.po", "id", "usb-imagewriter.mo")
    pisitools.domo("po/it.po", "it", "usb-imagewriter.mo")
    pisitools.domo("po/ja.po", "ja", "usb-imagewriter.mo")
    pisitools.domo("po/ka.po", "ka", "usb-imagewriter.mo")
    pisitools.domo("po/ko.po", "ko", "usb-imagewriter.mo")
    pisitools.domo("po/ml.po", "ml", "usb-imagewriter.mo")
    pisitools.domo("po/ms.po", "ms", "usb-imagewriter.mo")
    pisitools.domo("po/nb.po", "nb", "usb-imagewriter.mo")
    pisitools.domo("po/nl.po", "nl", "usb-imagewriter.mo")
    pisitools.domo("po/pl.po", "pl", "usb-imagewriter.mo")
    pisitools.domo("po/pt.po", "pt", "usb-imagewriter.mo")
    pisitools.domo("po/pt_BR.po", "pt_BR", "usb-imagewriter.mo")
    pisitools.domo("po/ro.po", "ro", "usb-imagewriter.mo")
    pisitools.domo("po/ru.po", "ru", "usb-imagewriter.mo")
    pisitools.domo("po/sk.po", "sk", "usb-imagewriter.mo")
    pisitools.domo("po/sv.po", "sv", "usb-imagewriter.mo")
    pisitools.domo("po/tr.po", "tr", "usb-imagewriter.mo")
    pisitools.domo("po/uk.po", "uk", "usb-imagewriter.mo")
    pisitools.domo("po/zh_CN.po", "zh_CN", "usb-imagewriter.mo")
    pisitools.domo("po/zh_HK.po", "zh_HK", "usb-imagewriter.mo")
    pisitools.domo("po/zh_TW.po", "zh_TW", "usb-imagewriter.mo")

    pisitools.insinto("/usr/share/","share/*")