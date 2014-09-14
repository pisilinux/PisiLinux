#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import qt4

#WorkDir = "QScintilla-gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.cd("Qt4Qt5")
    qt4.configure()

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4/")
    qt4.configure()

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

def build():
    shelltools.system("cp -rf Python Python3")
    shelltools.cd("Qt4Qt5")
    autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CXX()))

    shelltools.cd("../designer-Qt4/")
    autotools.make("DESTDIR=\"%s/%s/designer\"" % (get.installDIR(), qt4.plugindir))

    # Get Makefile of qscintilla-python via sip
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -p 4 -n ../Qt4Qt5 -o ../Qt4Qt5")
    autotools.make()
    shelltools.cd("../Python3")
    pythonmodules.run("configure.py -p 4 -n ../Qt4Qt5 -o ../Qt4Qt5", pyVer = "3")
    pisitools.dosed("Makefile", "-lpython3.4", "-lpython3")
    autotools.make()

def install():
    shelltools.cd("Qt4Qt5")
    qt4.install()

    shelltools.cd("../designer-Qt4/")
    qt4.install()

    #build and install qscintilla-python
    shelltools.cd("../Python3")
    autotools.install("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../Python")
    autotools.install("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4Qt5/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    pisitools.dodoc("GPL*", "LICENSE*", "NEWS", "README", "OPENSOURCE-NOTICE.TXT")
