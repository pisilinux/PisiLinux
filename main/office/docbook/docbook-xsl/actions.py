
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s/usr/share/xml/docbook/xsl-stylesheets"
                         % get.installDIR())
    pisitools.insinto("/usr/share/xml/docbook/xsl-stylesheets/","VERSION.xsl")

    # Don't ship the extensions
    pisitools.remove("/usr/share/xml/docbook/xsl-stylesheets/extensions/*")

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README",
                    "RELEASE-NOTES.txt", "TODO", "VERSION")
