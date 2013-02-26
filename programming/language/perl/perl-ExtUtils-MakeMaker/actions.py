#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_DOS.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::testlib.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Darwin.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_NW5.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Win95.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MakeMaker.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_UWIN.3pm")
    pisitools.remove("/usr/share/man/man1/instmodsh.1")
    pisitools.remove("/usr/share/man/man3/ExtUtils::Liblist.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Win32.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::Command::MM.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_MacOS.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Any.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_VOS.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MY.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_QNX.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_BeOS.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_VMS.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Cygwin.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_AIX.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MakeMaker::Tutorial.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_Unix.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MakeMaker::FAQ.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::Mkbootstrap.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::Mksymlists.3pm")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MM_OS2.3pm")
    pisitools.remove("/usr/bin/instmodsh")
    pisitools.remove("/usr/share/man/man3/ExtUtils::MakeMaker::Config.3pm")
      
    pisitools.dodoc("Changes", "MANIFEST", "README")
