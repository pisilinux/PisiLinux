#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    prefix = "/usr/share/icons/"
    klasor = ("Faenza", "Faenza-Ambiance", "Faenza-Dark", "Faenza-Darker", "Faenza-Darkest", "Faenza-Radiance")
    boyut = ("16", "22", "24", "32", "48", "64", "96", "128", "256")
    isim = ("distributor-logo-pisilinux.png", "pisilinux-logo.png", "start-here-kde.png", "start-here-pisilinux.png")

    for dosya in klasor:
        pisitools.insinto("/usr/share/icons", "%s" % dosya)

    for size in boyut:
        pisitools.dosym("%s%s/actions/%s/application-exit.png", "%s%s/actions/%s/cancel.png"% (prefix, dosya, size))

    for ad in isim:
        pisitools.dosym("/usr/share/icons/Faenza/places/% boyut/start-here.png", "%s%s/places/%s/%s"% (prefix, dosya, size, ad))
