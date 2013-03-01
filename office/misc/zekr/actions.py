#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s/%s" % (get.ARCH(), get.srcNAME())
BASEDIR = "/usr/share/java/zekr"

shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")
shelltools.export("JAVA_HOME","/opt/sun-jdk")

def setup():
    shelltools.system("ant clean")

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto(BASEDIR, "*")
    pisitools.dosym("%s/zekr.sh" % BASEDIR, "/usr/bin/zekr")

    pisitools.dodoc("doc/changes.txt", "doc/license/*", "doc/readme.txt")

    # Remove redundant files
    pisitools.removeDir("%s/build" % BASEDIR)
    pisitools.remove("%s/build.xml" % BASEDIR)
    pisitools.remove("%s/readme.txt" % BASEDIR)

    # Javadoc generation
    #shelltools.system("ant javadoc")
    #shelltools.copytree("build/docs/javadocs", "%s/%s/%s" %(get.installDIR(), get.docDIR(), get.srcNAME()))
    #shelltools.unlinkDir("%s%s/build" % (get.installDIR(), BASEDIR))
