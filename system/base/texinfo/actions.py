#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

TEX="/usr/share/texmf"

def setup():
    autotools.configure()

def build():
    autotools.make("TEXMF=TEX install-tex")

def install():
    pisitools.insinto("/usr/share/texmf", "%s/%s-%s/doc/TEX/tex" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    