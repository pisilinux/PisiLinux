#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dosed("bin/adduser.py", "plugdev", "removable")
    shelltools.system("./setup.py install %s" % get.installDIR())
    
    # in new tarball remove 
    shelltools.chmod(get.installDIR() + "/sbin/mudur_cgroupfs.py" , 0755)

    pisitools.dodir("/etc/mudur/services/enabled")
    pisitools.dodir("/etc/mudur/services/disabled")
    pisitools.dodir("/etc/mudur/services/conditional")
