#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("GOROOT", "%s/%s" % (get.workDIR(), get.srcNAME()))
shelltools.export("GOBIN", "$GOROOT/bin")
shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("GOROOT_FINAL", "/usr/lib/go")

shelltools.export("GOOS","linux")
shelltools.export("GOARCH","amd64")

def setup():

    shelltools.cd("src")
    shelltools.system("bash make.bash")

    #compile for emacs and xemacs
    shelltools.cd("../misc")
    shelltools.move("emacs/go-mode-load.el","emacs/golang-init.el")
    shelltools.system("cp -av emacs xemacs")

    shelltools.system("$GOROOT/bin/go get -d code.google.com/p/go.tools/cmd/godoc")
    shelltools.system("$GOROOT/bin/go build -o $GOPATH/godoc code.google.com/p/go.tools/cmd/godoc")

    for tool in ["cover", "vet"]:
        shelltools.system("$GOROOT/bin/go get -d code.google.com/p/go.tools/cmd/%s" % tool)
        shelltools.system("$GOROOT/bin/go build -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s code.google.com/p/go.tools/cmd/%s" % (tool, tool))


def install():  
    shelltools.cd("%s/go" % get.workDIR())
    pisitools.dobin("bin/*")
    pisitools.dodir("/usr/lib/go")
    pisitools.insinto("/usr/lib/go", "doc")
    pisitools.insinto("/usr/lib/go", "include")
    pisitools.insinto("/usr/lib/go", "lib")
    pisitools.insinto("/usr/lib/go", "pkg")
    pisitools.insinto("/usr/lib/go", "src")
    #vim
    pisitools.insinto("/usr/share/vim/vimfiles", "misc/vim/ftdetect")
    pisitools.insinto("/usr/share/vim/vimfiles", "misc/vim/ftplugin")
    pisitools.insinto("/usr/share/vim/vimfiles", "misc/vim/syntax")
    pisitools.insinto("/usr/share/vim/vimfiles", "misc/vim/indent")
    pisitools.insinto("/usr/share/vim/vimfiles", "misc/vim/plugin")
    #zsh
    pisitools.insinto("/usr/share/zsh/site-functions", "misc/zsh/go")

    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README", "AUTHORS", "CONTRIBUTORS")
