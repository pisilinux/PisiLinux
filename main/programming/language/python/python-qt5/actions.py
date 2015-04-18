#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PyQt-gpl-%s" % get.srcVERSION()

def setup():
  
    shelltools.copytree("%s/PyQt-gpl-5.4.1" % get.workDIR(), "%s/Py2Qt-gpl-5.4.1" % get.workDIR())
    pythonmodules.run("configure.py  --confirm-license \
                                     --assume-shared \
                                     --no-timestamp \
                                     --qsci-api \
                                     --enable=QtCore \
                                     --enable=QtWidgets \
                                     --enable=QtXml \
                                     --enable=QtGui \
                                     --sip /usr/local/bin/sip \
                                     --qmake='/usr/lib/qt5/bin/qmake' \
                                     --destdir='/usr/lib/python3.4/site-packages' \
                                     --sip-incdir='/usr/include/python3.4/sip3' \
                                     CFLAGS='%s' CXXFLAGS='%s'" % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
    
    shelltools.cd("%s/Py2Qt-gpl-5.4.1" % get.workDIR())
    shelltools.system("python configure.py  --confirm-license \
                                     --assume-shared \
                                     --no-timestamp \
                                     --qsci-api \
                                     --enable=QtCore \
                                     --enable=QtWidgets \
                                     --enable=QtXml \
                                     --enable=QtGui \
                                     --destdir='/usr/lib/python2.7/site-packages' \
                                     --sip-incdir='/usr/include/python2.7/sip3' \
                                     --sip /usr/local/bin/sip \
                                     --qmake='/usr/lib/qt5/bin/qmake'")
    #shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")    

def build():
    
    autotools.make()
    shelltools.cd("%s/Py2Qt-gpl-5.4.1" % get.workDIR())
    autotools.make()

def install():
  
    autotools.rawInstall("-C pyrcc DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C pylupdate DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    shelltools.cd("%s/Py2Qt-gpl-5.4.1" % get.workDIR())
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    #pisitools.rename("/usr/bin/pyuic5", "pyuic5-python")
    
    pisitools.dohtml("doc/html/*")
    
    pisitools.dodoc("NEWS", "README","LICENSE*")
