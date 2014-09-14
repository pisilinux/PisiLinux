#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "retroshare-0.5.5/src"

make_dirs = ["libbitdht","openpgpsdk","libretroshare","retroshare-gui","retroshare-nogui"]
binaries = ["retroshare-gui/src/RetroShare","retroshare-nogui/src/retroshare-nogui"]
symlinks = [["RetroShare","retroshare-gui"],["retroshare-nogui","retroshare-cli"]]
doc_files = ["libretroshare/src/Readme.txt","retroshare-gui/src/Todo.txt","retroshare-gui/src/license/*","libretroshare/src/TODO","libbitdht/src/README.txt"]
def setup():
	for dir in make_dirs:
		shelltools.cd("%s/%s/%s/src"%(get.workDIR(),WorkDir,dir))
		qt4.configure()

def build():
	for dir in make_dirs:
		shelltools.cd("%s/%s/%s/src"%(get.workDIR(),WorkDir,dir))
		qt4.make()

def install():
	for binary in binaries:
		pisitools.dobin("%s/%s/%s"%(get.workDIR(),WorkDir,binary))
	for sym in symlinks:
		pisitools.dosym("/usr/bin/%s"%sym[0],"/usr/bin/%s"%sym[1])
	pisitools.insinto("/usr/share/pixmaps/","%s/%s/retroshare-gui/src/gui/images/retrosharelogo2.png"%(get.workDIR(),WorkDir),"retroshare.png")
	for doc in doc_files:
		pisitools.dodoc("%s/%s/%s"%(get.workDIR(),WorkDir,doc))
