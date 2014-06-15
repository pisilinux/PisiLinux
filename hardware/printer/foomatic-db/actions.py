#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools

NoStrip = "/"

def setup():
    # For gutenprint printers, use gutenprint-ijs-simplified.5.2
    #pisitools.dosed("db/source/printer/*.xml", ">gutenprint<", ">gutenprint-ijs-simplified.5.2<")

    autotools.configure()

    # Cleanup conflicts
    #shelltools.cd("db/source")
    #shelltools.system("../../cleanup-conflicts")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fix permissions
    #for root, dirs, files in os.walk("%s/usr/share/foomatic/db" % get.installDIR()):
    #    for name in dirs:
    #        shelltools.chmod(os.path.join(root, name), 0755)
    #    for name in files:
    #        shelltools.chmod(os.path.join(root, name), 0644)
