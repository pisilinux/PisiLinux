#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s-nolibs-src" % (get.srcNAME(), get.srcVERSION())

shelltools.export("JAVA_HOME","/opt/sun-jdk")

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "dagitim/jar/*")
    pisitools.dosym("zemberek-az-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-az.jar")
    pisitools.dosym("zemberek-cekirdek-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-cekirdek.jar")
    pisitools.dosym("zemberek-demo-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-demo.jar")
    pisitools.dosym("zemberek-tk-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-tk.jar")
    pisitools.dosym("zemberek-tr-%s.jar" % get.srcVERSION(), "/usr/share/java/zemberek-tr.jar")

    pisitools.dodir(get.docDIR())
    shelltools.copytree("dokuman", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))

