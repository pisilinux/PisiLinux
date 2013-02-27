#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared \
                         --enable-imfexamples \
                         --enable-imffuzztest \
                         --disable-static")

def build():
    autotools.make()

def install():
    # documents and examples go to "/usr/share/OpenEXR" without these parameters
    docdir = "/usr/share/doc/%s" % get.srcNAME()
    examplesdir = "%s/examples" % docdir
    autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))

    pisitools.dodoc("AUTHORS", "ChangeLog","NEWS", "README","LICENSE")
