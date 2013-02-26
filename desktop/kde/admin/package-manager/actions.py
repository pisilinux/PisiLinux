#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

def install():
    pythonmodules.install()

    # Copy Notification Rc file for Kde 4
    pisitools.insinto("%s/package-manager/" % kde4.appsdir, "src/package-manager.notifyrc")

    for lang in ('de','en','es','fr','nl','sv','tr'):
        pisitools.insinto("%s/html/%s/package-manager/" % (kde4.docdir, lang),
                          "help/%s/main_help.html" % lang, "index.html")

    pisitools.remove('/usr/share/kde4/apps/package-manager/data/package-manager-*.desktop')

