#!/usr/bin/python

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/dfc/work/ and:
# WorkDir="dfc-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CHANGELOG", "README")
    
    pisitools.removeDir("/usr/etc/")

