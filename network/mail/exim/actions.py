#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
import shutil
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
import subprocess

def setup():
    shutil.copy("src/EDITME","Local/Makefile")
    shutil.copy("exim_monitor/EDITME","Local/eximon.conf")   
    pisitools.dosed("Local/Makefile","/usr/exim/bin","/usr/bin")
    pisitools.dosed("Local/Makefile","# CFLAGS_DYNAMIC=-shared -rdynamic -fPIC","CFLAGS_DYNAMIC=-shared -rdynamic")
    pisitools.dosed("Local/Makefile","# AUTH_PLAINTEXT=yes","AUTH_PLAINTEXT=yes")
    pisitools.dosed("Local/Makefile","# SUPPORT_TLS=yes","SUPPORT_TLS=yes")
    pisitools.dosed("Local/Makefile","# USE_GNUTLS=yes","USE_GNUTLS=yes")
    pisitools.dosed("Local/Makefile","# USE_GNUTLS_PC=gnutls","USE_GNUTLS_PC=gnutls")
    pisitools.dosed("Local/Makefile","# INFO_DIRECTORY=/usr/share/info","INFO_DIRECTORY=/usr/share/info")
    pisitools.dosed("Local/Makefile","# LOG_FILE_PATH=syslog:/var/log/exim_\\%slog","LOG_FILE_PATH=syslog")
    pisitools.dosed("Local/Makefile","ZCAT_COMMAND=/usr/bin/zcat","ZCAT_COMMAND=/usr/bin/gzip -c")
    pisitools.dosed("Local/Makefile","# EXIM_PERL=perl.o","EXIM_PERL=perl.o")
    pisitools.dosed("Local/Makefile","# EXTRALIBS_EXIM=-L/usr/local/lib -liconv","EXTRALIBS_EXIM=-L/usr/lib -ldl -export-dynamic -rdynamic")
    pisitools.dosed("Local/Makefile","# EXPAND_DLFUNC=yes","EXPAND_DLFUNC=yes")
    pisitools.dosed("Local/Makefile","# HAVE_IPV6=yes","HAVE_IPV6=yes")
    pisitools.dosed("Local/Makefile","/usr/exim/configure","/etc/exim/exim.conf")
    pisitools.dosed("Local/Makefile","EXIM_USER=","EXIM_USER=%s" % subprocess.check_output("",0,"/usr/bin/users").strip())
    
def build():
    autotools.make()

def install():
    pisitools.dodir("/var/spool/exim")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/man/man8","%s/%s/doc/exim.8" % (get.workDIR(),get.srcDIR()))
    pisitools.insinto("/usr/share/doc/exim","%s/%s/doc/*.txt" % (get.workDIR(),get.srcDIR()))
 
