#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
import shutil
import os
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#shelltools.export("USER","q")
WorkDir="sendmail-8.14.5"

def setup():
    shelltools.unlink("/%s/%s/devtools/bin/Build" % (get.workDIR(),get.srcDIR()))
    shelltools.move("/%s/%s/cf/Build" % (get.workDIR(),get.srcDIR()),"/%s/%s/devtools/bin/Build" % (get.workDIR(),get.srcDIR()))  
    os.rename("%s/%s/cf/cf/generic-linux.mc" % (get.workDIR(),get.srcDIR()),"%s/%s/cf/cf/sendmail.mc" % (get.workDIR(),get.srcDIR()))
    os.rename("%s/%s/cf/cf/generic-linux.cf" % (get.workDIR(),get.srcDIR()),"%s/%s/cf/cf/sendmail.cf" % (get.workDIR(),get.srcDIR()))
    
def build():
    shelltools.system('./Build')

def install():
    pisitools.dodir("/usr/sbin")
    pisitools.dodir("/var/spool/mqueue")
    pisitools.dodir("/var/spool/clientmqueue")
    pisitools.dodir("/usr/share/man/man8")
    pisitools.dodir("/usr/share/sendmail/cf")
    pisitools.dodir("/usr/share/sendmail/devtools")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())   
    shelltools.move("/%s/%s/sendmail/sendmail.8" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/man/man8" % get.installDIR())
    shelltools.move("/%s/%s/makemap/makemap.8" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/man/man8" % get.installDIR())
    shelltools.move("/%s/%s/editmap/editmap.8" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/man/man8" % get.installDIR())
    shelltools.move("/%s/%s/doc/op/op.ps" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/sendmail/guide" % get.installDIR())
    shelltools.move("/%s/%s/cf/cf/sendmail.cf" % (get.workDIR(),get.srcDIR()),"/%s/etc/mail/sendmail.cf" % get.installDIR())
    shelltools.move("/%s/%s/cf/*" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/sendmail/cf" % get.installDIR())
    shelltools.move("/%s/%s/devtools/*" % (get.workDIR(),get.srcDIR()),"/%s/usr/share/sendmail/devtools" % get.installDIR())
 
