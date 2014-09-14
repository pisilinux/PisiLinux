#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("fslint-gui","liblocation=os.path.*","liblocation = \'/usr/share/%s\'" % get.srcNAME())
    pisitools.dosed("fslint-gui","locale_base=.*","locale_base = None")

def install():
    # GUI executable
    pisitools.dobin("fslint-gui")

    insinto_dict = {# GUI file
            "/usr/share/fslint" : "fslint.glade",
            # icon
            "/usr/share/pixmaps" : "fslint_icon.png",
            # shortcut
            "/usr/share/applications" : "fslint.desktop"
            }

    for i in insinto_dict:
        pisitools.insinto(i, insinto_dict[i])

    doexe_dict= { # other executables
            "/usr/share/fslint/fslint" : ["fslint/find*", "fslint/zipdir", "fslint/fslint"] ,
            "/usr/share/fslint/fslint/fstool" : ["fslint/fstool/*"] ,
            "/usr/share/fslint/fslint/supprt" : ["fslint/supprt/get*", "fslint/supprt/fslver", "fslint/supprt/md5sum_approx"] ,
            "/usr/share/fslint/fslint/supprt/rmlint" : ["fslint/supprt/rmlint/*"] ,
            }

    for i in doexe_dict:
        pisitools.dodir(i)
        for j in doexe_dict[i]:
            pisitools.doexe(j, i)

    # locales
    shelltools.touch("Makefile")
    autotools.rawInstall("DESTDIR=%s -C po" % get.installDIR())

    # docs
    pisitools.dodoc("doc/*")

    # man files
    for i in ["man/fslint-gui.1", "man/fslint.1"]:
        pisitools.doman(i)

    # link to icon in main fslint dir
    pisitools.dosym("/usr/share/pixmaps/fslint_icon.png", "/usr/share/fslint/fslint_icon.png")

