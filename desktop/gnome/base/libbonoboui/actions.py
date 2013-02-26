#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --with-x")
    pisitools.dosed("libtool"," -shared "," -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    samples = ["/usr/lib/bonobo-2.0/samples/*",
               "/usr/lib/bonobo/servers/*.server",
               "/usr/share/gnome-2.0/ui/Bonobo_Sample_Hello.xml",
               "/usr/share/gnome-2.0/ui/Bonobo_Sample_Container-ui.xml"]
    for sample in samples:
        pisitools.remove(sample)

    pisitools.dodoc("NEWS", "README", "ChangeLog")
