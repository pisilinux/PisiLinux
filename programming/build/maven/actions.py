#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    shelltools.makedirs("%s/etc/profile.d" % get.installDIR())
    shelltools.makedirs("%s/usr/share/java/maven/lib" % get.installDIR())
    shelltools.makedirs("%s/usr/share/java/maven/boot" % get.installDIR())
    shelltools.makedirs("%s/usr/share/java/maven/conf" % get.installDIR())
    shelltools.makedirs("%s/usr/share/java/maven/bin" % get.installDIR())
    #shelltools.system(". /etc/profile.d/jre.sh")
    #shelltools.system(". /etc/profile.d/jdk.sh")
    shelltools.system("sed '42i\   <property name=\"maven.home\" value=\"%s/usr/share/java/maven-%s\"/>' build.xml > build2.xml" % (get.installDIR(), get.srcVERSION()))
    shelltools.system("mv build2.xml build.xml")
    shelltools.system("export M2_HOME=$maven.home")
    shelltools.system("export PATH=$PATH:$M2_HOME/bin")
    shelltools.system("export MAVEN_OPTS=-Xmx512m")
    shelltools.system("ant -Dmaven.repo.local=%s/usr/share/java/maven/repo" % get.installDIR())
    shelltools.system("mv %s/usr/share/java/maven-%s/bin/mvn %s/usr/share/java/maven/bin" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("mv %s/usr/share/java/maven-%s/bin/mvnDebug %s/usr/share/java/maven/bin" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("ln -s %s/usr/share/java/maven/bin/mvn %s/usr/bin/mvn" % (get.installDIR(), get.installDIR()))
    shelltools.system("ln -s %s/usr/share/java/maven/bin/mvnDebug %s/usr/bin/mvnDebug" % (get.installDIR(), get.installDIR()))
    shelltools.system("mv %s/usr/share/java/maven-%s/lib/* %s/usr/share/java/maven/lib/" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("mv %s/usr/share/java/maven-%s/boot/* %s/usr/share/java/maven/boot/" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("mv %s/usr/share/java/maven-%s/conf/* %s/usr/share/java/maven/conf/" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("mv %s/usr/share/java/maven-%s/bin/m2.conf %s/usr/share/java/maven/bin" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("rm -rf %s/usr/share/java/maven-%s" % (get.installDIR(), get.srcVERSION()))
    #shelltools.system("echo 'export M2_HOME=/usr/share/java/maven' >> /etc/profile.d")

