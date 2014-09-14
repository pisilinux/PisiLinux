# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # --shared and --release are default parameters, however we just write them
    # to down to avoid confusing wheter it's a static/shared or release/debug
    # package at the first look :)
    autotools.rawConfigure("--shared \
                            --release \
                            --dot dot \
                            --with-doxywizard \
                            --prefix /usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.doman("doc/doxywizard.1")

    # The makefile included is there to generate the html files
    # The user itself should execute it
    pisitools.insinto(get.docDIR() + "/doxygen" , "examples")

    pisitools.dodoc("LANGUAGE.HOWTO", "LICENSE", "README*", "VERSION")
