# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python2.7 --prefix=%s/usr" % get.installDIR())
    shelltools.echo("project-config.jam","using mpi ;")

def build():
    shelltools.system("./b2 stage threading=multi link=shared")

def install():
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())
    shelltools.system("./b2 install threading=multi link=shared")