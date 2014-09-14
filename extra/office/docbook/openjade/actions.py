#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docname = get.srcNAME()

def setup():
    shelltools.export("ALLOWED_FLAGS", "-O -O1 -O2 -pipe -g")
    shelltools.sym("config/configure.in", "configure.in")
    shelltools.export("SGML_PREFIX", "/usr/share/sgml")
    autotools.configure("--enable-http \
                         --enable-default-catalog=/etc/sgml/catalog \
                         --enable-default-search-path=/usr/share/sgml:/usr/share/xml \
                         --disable-static \
                         --enable-splibdir=/usr/lib \
                         --libdir=/usr/lib \
                         --datadir=/usr/share/sgml/%s" % docname)

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/lib")

    autotools.rawInstall("prefix=%s/usr \
                          libdir=%s/usr/lib \
                          datadir=%s/usr/share/sgml/%s " \
                          % (get.installDIR(), \
                             get.installDIR(), \
                             get.installDIR(), \
                             docname))

    pisitools.dosym("openjade", "/usr/bin/jade")
    pisitools.dosym("onsgmls", "/usr/bin/nsgmls")
    pisitools.dosym("osgmlnorm", "/usr/bin/sgmlnorm")
    pisitools.dosym("ospam", "/usr/bin/spam")
    pisitools.dosym("ospent", "/usr/bin/spent")
    pisitools.dosym("osx", "/usr/bin/sgml2xml")

    pisitools.insinto("/usr/share/sgml/%s" % docname, "dsssl/builtins.dsl")
    for i in ["dsssl/dsssl.dtd", "dsssl/style-sheet.dtd", "dsssl/fot.dtd"]:
        pisitools.insinto("/usr/share/sgml/%s/dsssl" % docname, i)
    pisitools.insinto("/usr/share/sgml/%s/pubtext" % docname, "pubtext/*")

    pisitools.dodoc("COPYING", "NEWS", "README", "VERSION")
    pisitools.dohtml("doc/*.htm")

    pisitools.insinto("/usr/share/doc/%s/jadedoc" % get.srcNAME(), "jadedoc/*.htm")
    pisitools.insinto("/usr/share/doc/%s/jadedoc/images" % get.srcNAME(), "jadedoc/images/*")


