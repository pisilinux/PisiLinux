#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --libexecdir=/usr/lib/mate-applets \
				    --disable-static \
				    --disable-scrollkeeper \
				    --disable-cpufreq \
				    --enable-polkit \
				    --enable-networkmanager \
				    --enable-mixer-applet \
				    --enable-mini-commander \
				    --enable-frequency-selector \
				    --enable-ipv6 \
				    --without-hal \
				    --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
    
    #pisitools.remove("/usr/share/mate-panel/applets/org.mate.applets.MixerApplet.mate-panel-applet")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-fi.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/eu/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-ru.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-pa.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/de/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ko/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ko/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/es/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ru/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-zh_CN.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-en_GB.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/C/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/el/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/es/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/de/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/pa/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ru/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/eu/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-it.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/en_GB/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/C/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-fr.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/hu/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-el.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ca/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-hu.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/zh_CN/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/hu/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/pt_BR/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/oc/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/pt_BR/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-da.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/fi/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/dbus-1/services/org.mate.panel.applet.MixerAppletFactory.service")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/zh_CN/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/en_GB/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/uk/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/it/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/fr/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-ko.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/cs/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/uk/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-ca.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-sv.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/da/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-de.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/it/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/cs/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/sv/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/da/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate-2.0/ui/mixer-applet-menu.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/C/legal.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-C.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-pt_BR.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/pa/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-oc.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-es.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/sv/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/oc/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/el/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-cs.omf")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/fi/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/ca/mate-mixer_applet2.xml")
    #pisitools.remove("/usr/share/mate/help/mate-mixer_applet2/fr/figures/volumecontrol_applet.png")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-uk.omf")
    #pisitools.remove("/usr/share/omf/mate-mixer_applet2/mate-mixer_applet2-eu.omf")
