#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("GOROOT", "%s/go-go1.4.2" % get.workDIR())
shelltools.export("GOBIN", "$GOROOT/bin")
shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("GOROOT_FINAL", "/usr/lib/go")

shelltools.export("GOOS","linux")
shelltools.export("GOARCH","amd64")

NoStrip=["/"]

def build():
    shelltools.cd("src")
    shelltools.system("bash make.bash")

    shelltools.cd("%s/go-go1.4.2" % get.workDIR())

    shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/godoc")
    shelltools.system("$GOROOT/bin/go build -o $GOPATH/godoc golang.org/x/tools/cmd/godoc")

    for tool in ["cover", "vet", "callgraph"]:
        shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
        shelltools.system("$GOROOT/bin/go build -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():  
    shelltools.cd("%s/go-go1.4.2" % get.workDIR())
    
    pisitools.dobin("bin/*")
    pisitools.dodir("/usr/lib/go")
    pisitools.insinto("/usr/lib/go", "doc")
    pisitools.insinto("/usr/lib/go", "include")
    pisitools.insinto("/usr/lib/go", "lib")
    pisitools.insinto("/usr/lib/go", "pkg")
    pisitools.insinto("/usr/lib/go", "src")

    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README", "AUTHORS", "CONTRIBUTORS")
