#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

MX_DIR = "/usr/lib/%s/site-packages/mx" % get.curPYTHON()

EMPTY_DIRS = ["BeeBase/Doc", "DateTime/Doc", "Doc", "Queue/Doc", "Stack/Doc", "TextTools/Doc", "Tools/Doc", "UID/Doc", \
              "URL/Doc", "DateTime/Examples", "TextTools/Examples"]

def install():
    pythonmodules.install()

    pisitools.dodoc("mx/LICENSE", "mx/COPYRIGHT")
    pisitools.dodoc("LICENSE", "COPYRIGHT", "MANIFEST", "README")


    # Make dir under docs for examples
    pisitools.dodir("%s/%s/Examples/DateTime" % (get.docDIR(), get.srcNAME()))
    pisitools.dodir("%s/%s/Examples/TextTools" % (get.docDIR(), get.srcNAME()))

    # Move examples from /usr/lib
    pisitools.domove("%s/DateTime/Examples/*.py" % MX_DIR, "%s/%s/Examples/DateTime/" % (get.docDIR(), get.srcNAME()))
    pisitools.domove("%s/TextTools/Examples/*.py" % MX_DIR, "%s/%s/Examples/TextTools/" % (get.docDIR(), get.srcNAME()))
