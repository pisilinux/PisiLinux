#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    
    pisitools.rename("/usr/lib/python2.7/site-packages/synaptiks/kde/widgets/ui/touchpadinformationwidget.ui", "touchpadInformationwidget.ui")
    pisitools.insinto("/usr/share/autostart/", "autostart/synaptiks_autostart.desktop")
    pisitools.insinto("/etc/xdg/autostart/", "autostart/synaptiks_init_config.desktop")
    pisitools.insinto("/usr/share/kde4/services/", "services/kcm_synaptiks.desktop")
    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps/", "pics/synaptiks.svgz")
    pisitools.insinto("/usr/share/pixmaps/", "pics/synaptiks.svgz")
    pisitools.insinto("/usr/share/kde4/apps/synaptiks/pics/", "pics/off-overlay.svgz")
    pisitools.insinto("/usr/share/kde4/apps/synaptiks/", "synaptiks.notifyrc")
    pisitools.insinto("/usr/share/kde4/apps/synaptiks/", "services/kcm_synaptiks.py")
    pisitools.insinto("/etc/xdg/autostart/", "autostart/synaptiks_init_config.desktop")
    pisitools.insinto("/usr/share/applications/kde4/", "synaptiks.desktop")
    
    pisitools.domo("po/cs.po", "cs", "synaptiks.mo")
    pisitools.domo("po/da.po", "da", "synaptiks.mo")
    pisitools.domo("po/de.po", "de", "synaptiks.mo")
    pisitools.domo("po/fr.po", "fr", "synaptiks.mo")
    pisitools.domo("po/it.po", "it", "synaptiks.mo")
    pisitools.domo("po/ru.po", "ru", "synaptiks.mo")
    pisitools.domo("po/uk.po", "uk", "synaptiks.mo")
    pisitools.domo("po/po_synaptiks-tr.po", "tr", "synaptiks.mo")