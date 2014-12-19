# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

binDir = "bin.linuxx86"

def setup():
    shelltools.echo("%s/boost_1_57_0/project-config.jam" % get.workDIR(),"using python : 2.7 : /usr/bin/python ; ")
    shelltools.echo("%s/boost_1_57_0/project-config.jam" % get.workDIR(),"using python : 3.2 : /usr/bin/python3 : /usr/include/python3.2mu : /usr/lib ;")
    shelltools.echo("%s/boost_1_57_0/project-config.jam" % get.workDIR(),"using mpi ;")


def build():
    shelltools.system("./bootstrap.sh")

    #shelltools.cd("%s/%s/tools/build/v2/engine" % (get.workDIR(),WorkDir))
    #shelltools.system("./build.sh cc")

    #if get.ARCH() == "x86_64":
    #  binDir = "bin.linuxx86_64"

    #shelltools.cd(binDir)
    #shelltools.system("./bjam --toolset=gcc ../../../../")
    #shelltools.copy("bjam","%s/%s/dist/bin/bjam" % (get.workDIR(),WorkDir))
    #shelltools.cd("%s/%s" % (get.workDIR(),WorkDir))
    #shelltools.system("dist/bin/bjam release debug-symbols=off threading=multi \
	#		runtime-link=shared link=shared,static \
	#		cflags=-fno-strict-aliasing \
	#		toolset=gcc \
	#		--prefix=dist/ \
	#		-sTOOLS=gcc \
	#		--layout=system")

def install():
    pisitools.dodir("/usr")
    shelltools.system("./b2 install --prefix=%s/usr" % get.installDIR());