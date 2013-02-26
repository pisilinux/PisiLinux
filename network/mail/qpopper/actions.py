#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
import subprocess

WorkDir="qpopper4.1.0"
cfg=""
if get.ARCH() == "x86_64":
    cfg="--enable-64-bit "
else:
    cfg="--enable-32-bit "
        

def setup():
    pisitools.dosed("./popper/Makefile.in","\\$\\{installdir\\}/\\$\\{pop_auth\\} -init -safe;","")
    autotools.configure("%s--enable-spool-dir=/var/spool/mail --enable-servermode --enable-specialauth --enable-apop=/etc/pop.auth --enable-log-login \
			 --enable-server-mode-group-include=users --enable-poppassd --enable-popuid=%s --with-openssl=/usr/lib/openssl --with-gdbm=/usr/lib" % (cfg,subprocess.check_output("",0,"/usr/bin/users").strip())) 

		#--enable-bulldb=/var/spool/bulls,--with-kerberos5=/usr/lib >>missing header(<et/com_err.h>) ve undefined reference(db.h'ta tanımlı) veriyor.biara fixlerim.

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")
    autotools.install()

    #pisitools.removeDir("/usr/share")

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "doc/liblink", "doc/libroutines")
