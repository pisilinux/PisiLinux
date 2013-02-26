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

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-clipart \
                         --enable-templates \
                         --enable-plugins \
                         --with-pic \
                         --with-gnomevfs")
    """
    configure: WARNING: mathview plugin: dependencies not satisfied - mathview-frontend-libxml2 >= 0.7.5
    configure: WARNING: ots plugin: dependencies not satisfied - libots-1 >= 0.5.0
    configure: WARNING: gda plugin: dependencies not satisfied - libgda >= 1.2.0 libgnomedb >= 1.2.0
    configure: WARNING: wpg plugin: dependencies not satisfied - libgsf-1 >= 1.12 libwpg-0.1 >= 0.1.0 libwpd-0.8 >= 0.8.0
    configure: WARNING: rsvg plugin: not needed with gtk
    configure: WARNING: aiksaurus plugin: dependencies not satisfied - gaiksaurus-1.0
    configure: WARNING: grammar plugin: dependencies not satisfied - link-grammar >= 4.2.1
    configure: WARNING: wordperfect plugin: dependencies not satisfied - libwpd-0.8 >= 0.8.0 libgsf-1 >= 1.12
    configure: WARNING: psiconv plugin: program psiconv-config not found in path
    """

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

