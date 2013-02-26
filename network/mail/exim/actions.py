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
    shutil.copy("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/src/EDITME","/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile")
    shutil.copy("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/exim_monitor/EDITME","/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/eximon.conf")   
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/usr/exim/bin","/usr/bin")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# CFLAGS_DYNAMIC=-shared -rdynamic -fPIC","CFLAGS_DYNAMIC=-shared -rdynamic")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# AUTH_PLAINTEXT=yes","AUTH_PLAINTEXT=yes")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# SUPPORT_TLS=yes","SUPPORT_TLS=yes")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# USE_GNUTLS=yes","USE_GNUTLS=yes")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# USE_GNUTLS_PC=gnutls","USE_GNUTLS_PC=gnutls")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# INFO_DIRECTORY=/usr/share/info","INFO_DIRECTORY=/usr/share/info")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# LOG_FILE_PATH=syslog:/var/log/exim_\\%slog","LOG_FILE_PATH=syslog")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","ZCAT_COMMAND=/usr/bin/zcat","ZCAT_COMMAND=/usr/bin/gzip -c")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# EXIM_PERL=perl.o","EXIM_PERL=perl.o")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# EXTRALIBS_EXIM=-L/usr/local/lib -liconv","EXTRALIBS_EXIM=-L/usr/lib -ldl -export-dynamic -rdynamic")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# EXPAND_DLFUNC=yes","EXPAND_DLFUNC=yes")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","# HAVE_IPV6=yes","HAVE_IPV6=yes")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/usr/exim/configure","/etc/exim/exim.conf")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","EXIM_USER=","EXIM_USER=%s" % subprocess.check_output("",0,"/usr/bin/users").strip())
    #pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/var/spool/exim","/var/spool/exim")
    
def build():
    autotools.make()

def install():
    pisitools.dodir("/var/spool/exim")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/man/man8","%s/%s/doc/exim.8" % (get.workDIR(),get.srcDIR()))
    pisitools.insinto("/usr/share/doc/exim","%s/%s/doc/*.txt" % (get.workDIR(),get.srcDIR()))
    #pisitools.rename("/usr/bin/exim-4.80.1-3","exim")
 
