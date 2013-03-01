# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("%s/%s/doc/auctex.info" % (get.workDIR(), get.srcDIR()))

    autotools.configure("EMACS_NAME=emacs EMACS_FLAVOUR=emacs econf --disable-build-dir-test \
                         --with-auto-dir='/var/lib/auctex' \
                         --with-lispdir='/usr/share/emacs/site-lisp/%s' \
                         --with-packagelispdir='/usr/share/emacs/site-lisp/%s' \
                         --with-packagedatadir='/usr/share/emacs/etc/%s'" \
                         % (get.srcNAME(),get.srcNAME(),get.srcNAME()))

def build():
    autotools.make()

    shelltools.cd("doc/")
    autotools.make("tex-ref.pdf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    pisitools.dodoc("CHANGES", "ChangeLog", "README", "COPYING", "FAQ", "RELEASE", "TODO", "doc/tex-ref.pdf")
