#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("export LC_ALL=en_US.UTF-8")
    pisitools.flags.add("-std=c++11")
    autotools.configure("--prefix=/usr/lib/jvm/java-7-openjdk\
                         --datarootdir=/usr/share \
                         --with-jdk-home=/usr/lib/jvm/java-7-openjdk \
                         --with-browser-tests \
                         --disable-docs \
                         --with-firefox=/usr/bin/firefox \
                         --with-chromium=/usr/bin/chromium-browser")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/lib/jvm/java-7-openjdk/lib/IcedTeaPlugin.so", "/usr/lib/browser-plugins/IcedTeaPlugin.so")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
