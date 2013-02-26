#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "webkitgtk-1.11.1"

shelltools.export("HOME", get.workDIR())
shelltools.export("XDG_DATA_HOME", get.workDIR())
shelltools.export("CXXFLAGS", get.CXXFLAGS().replace(" -ggdb3", ""))

opt = " -fPIC" if get.ARCH() == "x86_64" else ""
paths = ["JavaScriptCore", "WebCore", "WebKit"]
docs = ["AUTHORS", "ChangeLog", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    pisitools.dosed("configure", " -O2", opt)
    autotools.configure("--enable-dependency-tracking \
                         --with-gnu-ld \
                         --enable-introspection \
                         --enable-video \
                         --enable-filters \
                         --with-font-backend=pango \
                         --with-unicode-backend=icu \
                         --with-gtk=2.0 \
                         --disable-webkit2 \
                         --disable-gtk-doc")
    pisitools.dosed("GNUmakefile", "(Programs_DumpRenderTree_LDFLAGS\s=\s)", r"\1-lfontconfig ")

def build():
    autotools.make("DerivedSources/WebCore/JSNode.h")
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    # remove empty dir
    pisitools.removeDir("usr/libexec")

    #pisitools.domove("/usr/share/gtk-doc/html/webkitgtk", "/usr/share/gtk-doc/html/webkitgtk2")

    pisitools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
