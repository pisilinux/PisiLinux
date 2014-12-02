#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

NoStrip = ["/usr/bin", "/usr/lib", "/usr/qt/4/qsci/api"]
conf = {"bindir": "/usr/bin",
        "installdir": get.installDIR(),
        "site-packages": "/usr/lib/python3.3/site-packages"}

def install():
    pythonmodules.run("install.py -z \
                                  -b %(bindir)s \
                                  -i %(installdir)s \
                                  -d %(site-packages)s \
                                  -c" % conf, pyVer = "3")
    pythonmodules.fixCompiledPy()
    for lang in ["cs", "de", "es", "fr", "it", "ru", "tr"]:
        pisitools.insinto("%(site-packages)s/eric5/i18n" % conf, "eric/i18n/eric5_%s.qm" % lang)
    pisitools.dodoc("changelog", "LICENSE.GPL3", "THANKS", "README*")
#    pisitools.insinto("/usr/lib/python3.3/site-packages/", "/usr/lib/python3.3/site-packages/eric5config.py")
    # remove files conflict with eric4
    pisitools.remove("/usr/share/qt4/qsci/api/python/zope-2.11.2.api")
    pisitools.remove("/usr/share/qt4/qsci/api/python/zope-2.10.7.api")
    pisitools.remove("/usr/share/qt4/qsci/api/python/zope-3.3.1.api")
    pisitools.remove("/usr/share/qt4/qsci/api/ruby/Ruby-1.8.7.api")
