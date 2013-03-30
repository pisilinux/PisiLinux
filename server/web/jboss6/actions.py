#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
JBOSS_HOME = "/opt/jboss6"

NoStrip = ["/"]

def install():
    pisitools.dodir(JBOSS_HOME)
    pisitools.insinto(JBOSS_HOME, "jboss-6.0.0.Final/*")

    shelltools.cd("./jboss-6.0.0.Final/")

    # For support JAX-WS 2.0 in java 6 environment
    #for f in ("jbossws-native-jaxrpc.jar", "jbossws-native-jaxws-ext.jar", "jbossws-native-jaxws.jar", "jbossws-native-saaj.jar"):
    #    pisitools.insinto("%s/lib/endorsed" % JBOSS_HOME, "client/%s" % f)

    # Doc operations
    #pisitools.dodoc("lgpl.html", "readme.html")
    #for f in ("lgpl.html", "readme.html"):
    #    pisitools.remove("%s/%s" %(JBOSS_HOME, f))

    # Remove unsupported files
    pisitools.remove("%s/bin/*bat" % JBOSS_HOME)
    pisitools.remove("%s/bin/*exe" % JBOSS_HOME)
