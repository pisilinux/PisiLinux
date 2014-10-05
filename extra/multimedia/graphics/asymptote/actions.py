#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --includedir=/usr/include \
                         --with-docdir=/usr/share/doc/asymptote \
                         --enable-gsl \
                         --enable-gc=system \
                         --enable-texlive-build \
                         --with-latex=/usr/share/texmf-dist/tex/latex \
                         --with-context=/usr/share/texmf-dist/tex/context")

                         

def build():   
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add files for emacs users
    pisitools.domove("/usr/share/asymptote/*.el", "/usr/share/emacs/site-lisp/")
    pisitools.domove("/usr/share/asymptote/*.vim", "/usr/share/vim/vimfiles/ftdetect/")

    # move file to correct path.
    #pisitools.domove("/usr/local/share/texmf/tex/context/third/asymptote/colo-asy.tex", "/usr/share/texmf/tex/context/third/asymptote/")
    #pisitools.removeDir("/usr/local")
