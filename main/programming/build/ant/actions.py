#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import glob

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

WorkDir = "apache-ant-%s" % get.srcVERSION()
anthome = "/usr/share/ant"
javadir = "/usr/share/java"

def build():
    shelltools.system("./build.sh")

def install():
    for d in (anthome, os.path.join(anthome, "lib"), os.path.join(anthome, "etc"), os.path.join(anthome, "bin"), javadir, os.path.join(javadir, "ant")):
        pisitools.dodir(d)

    shelltools.cd("build/lib")

    for f in ("ant.jar", "ant-launcher.jar", "ant-bootstrap.jar"):
        pisitools.insinto(javadir, f, f.replace(".jar", "-%s.jar" % get.srcVERSION()))
        pisitools.dosym(os.path.join(javadir, f.replace(".jar", "-%s.jar" % get.srcVERSION())), os.path.join(anthome, "lib", f))
        pisitools.dosym(os.path.join(javadir, f.replace(".jar", "-%s.jar" % get.srcVERSION())), os.path.join(javadir, f))

    #Install optional JAR files to /usr/share/java/ant
    for f in ("ant-jmf.jar", "ant-junit.jar", "ant-swing.jar"):
        pisitools.insinto(os.path.join(javadir, "ant"), f, f.replace(".jar", "-%s.jar" % get.srcVERSION()))
        pisitools.dosym(os.path.join(javadir, "ant", f.replace(".jar", "-%s.jar" % get.srcVERSION())), os.path.join(anthome, "lib", f))
        pisitools.dosym(os.path.join(javadir, "ant", f.replace(".jar", "-%s.jar" % get.srcVERSION())), os.path.join(javadir, "ant", f))


    shelltools.cd("../../src/script")
    for f in glob.glob("*.bat"):
        shelltools.unlink(f)

    for f in glob.glob("*.cmd"):
        shelltools.unlink(f)

    pisitools.dobin("*")
    pisitools.domove("/usr/bin/antRun*", os.path.join(anthome, "bin"))
    shelltools.cd("../../")

    #Install XSLs
    pisitools.insinto(os.path.join(anthome, "etc"), "src/etc/*.xsl")

    pisitools.dodoc("KEYS", "NOTICE", "README", "WHATSNEW", "LICENSE")
    #pisitools.dohtml("docs/*")
