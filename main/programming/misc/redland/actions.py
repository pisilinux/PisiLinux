#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    for i in ["librdf.h", "rdf_init.h"]:
        pisitools.dosed("src/%s" % i, "<rasqal.h>", "<rasqal/rasqal.h>")

    autotools.autoreconf("-vfi")

    #Caution!!! --enable-storages option is buggy! Do not use it, it causes storages other than memory not to be compiled!! And it's enabled by default!!
    #Using iODBC driver manager instead of unixODBC, as unixODBC needs to be compiled statically.
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --with-raptor=system \
                         --with-rasqal=system \
                         --with-sqlite=3 \
                         --with-virtuoso \
                         --with-iodbc=/%s \
                         --without-unixodbc \
                         " % get.defaultprefixDIR())
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README")
