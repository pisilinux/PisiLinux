#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = '/%s/%s' % (get.docDIR(), get.srcNAME())

def setup():
    pisitools.dosed("sylpheed.desktop", "Icon=sylpheed", "Icon=sylpheed-128x128")
    autotools.configure("--enable-ldap \
                         --enable-compface \
                         --disable-updatecheck \
                         --disable-updatecheckplugin \
                         --disable-static \
                         --with-manualdir=%s \
                         --with-faqdir=%s" % (docdir, docdir))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/pixmaps")
    pisitools.insinto("/usr/share/pixmaps", "*.png")

    pisitools.insinto("/usr/share/applications", "sylpheed.desktop")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS*", "README*", "TODO*", "PLUGIN.txt", "ABOUT-NLS")

    pisitools.dodir("/usr/lib/sylpheed/plugins")
    pisitools.insinto("/usr/lib/sylpheed/plugins", "plugin/attachment_tool/.libs/attachment_tool.so")

    for lang in ["en", "de", "es", "fr", "it", "ja"]:
        pisitools.domove("/usr/share/doc/sylpheed/%s" % lang, "/usr/share/doc/sylpheed/html/")
