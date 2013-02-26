#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-gc=system \
                         --with-latex=/usr/share/texmf-dist/tex/latex")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add files for emacs users
    pisitools.domove("/usr/share/asymptote/*.el", "/usr/share/emacs/site-lisp/")

    # move file to correct path.
    pisitools.domove("/usr/local/share/texmf/tex/context/third/asymptote/colo-asy.tex", "/usr/share/texmf/tex/context/third/asymptote/")
    pisitools.removeDir("/usr/local")
