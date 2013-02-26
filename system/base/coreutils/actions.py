#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


movetobin = ["arch", "basename", "cat", "chgrp", "chmod", "chown", "cp", "cut", "date", "dd", "df",
             "dir", "echo", "env", "false", "link", "ln", "ls", "mkdir", "mknod", "mktemp", "mv",
             "nice", "pwd", "readlink", "rm", "rmdir", "sleep", "sort", "stty", "sync", "touch",
             "true", "uname", "unlink", "vdir"]

symtousrbin = ["env", "cut", "readlink"]

def setup():
    shelltools.export("gl_cv_func_printf_directive_n", "yes")
    shelltools.export("gl_cv_func_isnanl_works", "yes")
    # shelltools.export("DEFAULT_POSIX2_VERSION", "199209")
    shelltools.export("DEFAULT_POSIX2_VERSION", "200112")
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -fPIC -D_GNU_SOURCE=1 " % get.CFLAGS())
    shelltools.export("FORCE_UNSAFE_CONFIGURE","1")
    shelltools.export("AT_M4DIR", "m4")
    autotools.autoreconf("-vfi")

    # Fedora also installs su and hostname
    autotools.configure("--enable-largefile \
                         --enable-install-program=arch \
                         --enable-no-install-program=faillog,hostname,login,lastlog,uptime \
                         --libexecdir=/usr/lib")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def check():
    # check does horrible things like modifying mtab or loop mounting
    # use it if you are too curious
    # autotools.make("check")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make("mandir=%s/%s install-man" % (get.installDIR(), get.manDIR()))
    #~ autotools.install("mandir=%s/%s" % (get.installDIR(), get.manDIR()))

    # Use dircolors from the package
    pisitools.insinto("/etc", "src/dircolors.hin", "DIR_COLORS")

    # move critical files into /bin
    for f in movetobin:
        pisitools.domove("/usr/bin/%s" % f, "/bin/")

    for f in symtousrbin:
        pisitools.dosym("../../bin/%s" % f, "/usr/bin/%s" % f)

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")

