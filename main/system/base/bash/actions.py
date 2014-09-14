#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


cfgsettings = """-DDEFAULT_PATH_VALUE=\'\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\' \
                 -DSTANDARD_UTILS_PATH=\'\"/bin:/usr/bin:/sbin:/usr/sbin\"\' \
                 -DSYS_BASHRC=\'\"/etc/bash/bashrc\"\' \
                 -DNON_INTERACTIVE_LOGIN_SHELLS \
                 -DSSH_SOURCE_BASHRC"""
                 #-DSYS_BASH_LOGOUT=\'\"/etc/bash/bash_logout\"\' \

def setup():
    # Recycles pids is neccessary. When bash's last fork's pid was X and new fork's pid is also X,
    # bash has to wait for this same pid. Without Recycles pids bash will not wait.
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -DRECYCLES_PIDS %s " % (get.CFLAGS(), cfgsettings))

    autotools.autoconf()
    autotools.configure("--without-installed-readline \
                         --disable-profiling \
                         --without-gnu-malloc \
                         --disable-rpath \
                         --with-curses")

def build():
    autotools.make()

# FIXME: package build stops right after checking even when no errors happen (probably
# due to SIGHUP in test). It is the duty of the packager to run tests by hand.
#def check():
#    autotools.make("check")

def install():
    autotools.install()

    pisitools.domove("/usr/bin/bash", "/bin")
    pisitools.dosym("/bin/bash","/bin/sh")
    pisitools.dosym("/bin/bash","/bin/rbash")

    # Compatibility with old skels
    # pisitools.dosym("/etc/bash/bashrc", "/etc/bashrc")

    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
