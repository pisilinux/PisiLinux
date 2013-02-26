#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

InstDir = get.installDIR()
manDir = get.manDIR()


def setup():
    autotools.rawConfigure("--with-diffutils \
                            --prefix=/%s \
                            --host=%s \ " %
                            (get.defaultprefixDIR(), \
                             get.HOST()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr \
                          man1dir=%s/%s/man1 \
                          man3dir=%s/%s/man3 \
                          man5dir=%s/%s/man5" %
                          (InstDir,InstDir,manDir,InstDir,
                          manDir,InstDir,manDir))
    pisitools.dodoc("ChangeLog", "CREDITS", "NEWS", "README", "REFS")
