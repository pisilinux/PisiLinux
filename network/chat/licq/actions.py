#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

shelltools.export("LDFLAGS", "%s -pthread" % get.LDFLAGS())
shelltools.export("HOME", get.workDIR())

# Optional Plugins, Licq need at least one plugin to work
plugins = ["auto-reply", \
           "console", \
           "forwarder", \
           "jabber" , \
           "msn", \
           "osd", \
           "qt4-gui", \
           "rms"]

def setup():
    cmaketools.configure()
    for name in plugins:
        shelltools.cd("plugins/%s" % name)
        cmaketools.configure(" -DCMAKE_MODULE_PATH=%s/%s/cmake -DLicq_INCLUDE_DIR=%s/%s/include" % (get.workDIR(), get.srcDIR(), get.workDIR(), get.srcDIR()))
        shelltools.cd("../..")

def build():
    cmaketools.make()
    for name in plugins:
        shelltools.cd("plugins/%s" % name)
        cmaketools.make()
        shelltools.cd("../..")

def install():
    cmaketools.install()
    for name in plugins:
        shelltools.cd("plugins/%s" % name)
        autotools.rawInstall('DESTDIR="%s"'  % get.installDIR())
        shelltools.cd("../..")

    # Licq-web plugin
    pisitools.dodir("/var/www/localhost/htdocs")
    pisitools.insinto("/var/www/localhost/htdocs/", "plugins/licqweb/")

    pisitools.dodoc("README", "README.GPG", "README.OPENSSL", "doc/*")
