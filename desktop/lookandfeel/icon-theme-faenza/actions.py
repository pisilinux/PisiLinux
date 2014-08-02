#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    path = "/usr/share/icons"
    klasor = ("Faenza", "Faenza-Ambiance", "Faenza-Dark", "Faenza-Darker", "Faenza-Darkest", "Faenza-Radiance")
    boyut = ("16", "22", "24", "32", "48", "64", "96", "128", "256")

    for dosya in klasor:
        pisitools.insinto("/usr/share/icons", dosya)

        for size in boyut:
            pisitools.dosym("application-exit.png", "%s/%s/actions/%s/cancel.png"% (path, dosya, size))
