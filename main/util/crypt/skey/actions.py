#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Note that we fiddle with permissions of everything to make sure not to make a security hole
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
    shelltools.export("SENDMAIL", "/usr/sbin/sendmail")
    shelltools.export("CFLAGS", "%s -DSKEY_HASH_DEFAULT=1" % get.CFLAGS())
    autotools.configure("--sysconfdir=/etc/skey")

def build():
    autotools.make()

def install():
    ### Runtime
    for i in ["skey", "skeyinit", "skeyinfo"]:
        pisitools.dobin(i)

    for i in ["otp-md4", "otp-sha1", "otp-md5"]:
        pisitools.dosym("skey", "/usr/bin/%s" % i)

    pisitools.insinto("/usr/sbin", "skeyprune.pl", "skeyprune")
    pisitools.insinto("/usr/bin", "skeyaudit.sh", "skeyaudit")

    # these must be suid root so users can generate their passwords, fperms u+s,og-r
    for i in ["skeyinit", "skeyinfo", "skeyaudit"]:
        shelltools.chmod("%s/usr/bin/%s" % (get.installDIR(), i), 4755)

    shelltools.chmod("%s/usr/bin/skey" % get.installDIR(), 0755)
    shelltools.chmod("%s/usr/sbin/skeyprune" % get.installDIR(), 0755)


    ### Developement
    pisitools.insinto("/usr/include", "skey.h")

    for i in ["libskey.so.1.1.5", "libskey.so.1", "libskey.so"]:
        # dolib borks with symlinks
        # pisitools.dolib(i, destinationDirectory="/lib")
        pisitools.insinto("/lib", i)
        shelltools.chmod("%s/lib/%s" % (get.installDIR(), i), 0755)

    #libtools.gen_usr_ldscript("libskey.so")
    pisitools.dosym("../../lib/libskey.so", "/usr/lib/libskey.so")


    ### Config
    # only root needs to have access to these files. fperms g-rx,o-rx /etc/skey
    pisitools.dodir("/etc/skey")
    shelltools.chmod("%s/etc/skey" % get.installDIR(), 0700)

    # skeyinit will not function if this file is not present. these permissions are applied by the skey system if missing.
    shelltools.touch("%s/etc/skey/skeykeys" % get.installDIR())
    shelltools.chmod("%s/etc/skey/skeykeys" % get.installDIR(), 0600)


    ### Docs
    for i in ["skey.1", "skeyaudit.1", "skeyinfo.1", "skeyinit.1", "skey.3", "skeyprune.8"]:
        pisitools.doman(i)

    pisitools.dodoc("CHANGES", "README")

