#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-database=db \
                         --disable-rpath \
                         --without-included-gsl \
                         --disable-transactions")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("contrib/bfproxy.pl")
    pisitools.dobin("contrib/bogominitrain.pl")
    pisitools.dobin("contrib/mime.get.rfc822.pl")
    pisitools.dobin("contrib/printmaildir.pl")
    pisitools.dobin("contrib/spamitarium.pl")
    pisitools.dobin("contrib/stripsearch.pl")
    pisitools.dobin("contrib/trainbogo.sh")

    pisitools.rename("/etc/bogofilter.cf.example","bogofilter.cf")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS*", "README",
                    "RELEASE.NOTES*", "TODO", "GETTING.STARTED",
                    "gpl-3.0.txt",
                    "doc/integrating-with-*",
                    "contrib/bogofilter-qfe.sh",
                    "contrib/bogofilter-milter.pl",
                    "contrib/dot-qmail-bogofilter-default",
                    "contrib/*.example",
                    "contrib/parmtest.sh",
                    "contrib/README.*",
                    "contrib/randomtrain.sh",
                    "contrib/scramble.sh")

