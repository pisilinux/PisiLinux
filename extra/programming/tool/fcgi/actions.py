#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "%s-%s-SNAP-0311112127" % (get.srcNAME(), get.srcVERSION())

def setup():
    libtools.libtoolize("--copy --force")
    autotools.aclocal()
    autotools.configure("--enable-static=no")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE.TERMS", "README")
    pisitools.dohtml("doc/*.html", "doc/*.gif", "doc/fastcgi-prog-guide/*.*", "doc/fastcgi-whitepaper/*.*")
    pisitools.doman("doc/cgi-fcgi.1", "doc/FCGI_Accept.3", "doc/FCGI_Finish.3", "doc/FCGI_SetExitStatus.3", "doc/FCGI_StartFilterData.3")

