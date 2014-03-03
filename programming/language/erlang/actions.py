#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir="otp_src_R%sB0%s" % (get.srcVERSION().split(".")[0], get.srcVERSION().split(".")[1])

# For finding javac, javadoc
shelltools.export("PATH", "%s:/usr/lib/jvm/java-7-openjdk/bin" % (os.environ.get("PATH")))

def setup():
    # Remove bundled zlib
    shelltools.unlink("erts/emulator/zlib/*.[ch]")

    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.configure("--enable-shared-zlib \
                         --enable-dynamic-ssl-lib \
                         --enable-threads \
                         --enable-kernel-poll \
                         --enable-hipe \
                         --enable-smp-support \
                         --with-ssl ac_cv_prog_FOP=")

def build():
    autotools.make("-j1")

    # Building documentation needs escript from erlang package
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), os.environ.get("PATH")))
    autotools.make("-j1 docs")

def install():
    # Build dummy PDFs to break fop dependency
    shelltools.system("./genpdf")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-docs" % get.installDIR())

    # Cleanup package
    pisitools.remove("/usr/lib/erlang/Install")

    # Remove win32 stuff, old txt files, object files, etc.
    for f in ("lib/observer-*/priv/bin/*.bat",
              "lib/os_mon-*/ebin/nteventlog.beam",
              "lib/ssl-*/examples/certs/etc/otpCA/*.txt.old",
              "lib/webtool-*/priv/bin/start_webtool.bat",
              "lib/*-*/info",
              "erts-*/info",
              "man/man3/erl_set_memory_block.*",
              "man/man3/nteventlog.*",
              "man/man3/win32reg.*",
              "man/man1/erlsrv.*",
              "man/man1/werl.*",
              "PR.template",
              ):
        pisitools.remove("/usr/lib/erlang/%s" % f)

    # Move README and COPYRIGHT
    pisitools.domove("/usr/lib/erlang/README", "/usr/share/doc/%s" % get.srcNAME())
    pisitools.domove("/usr/lib/erlang/COPYRIGHT", "/usr/share/doc/%s" % get.srcNAME())

    for d in ("lib/*/priv/obj",
              "lib/*/c_src",
              "lib/*/java_src",
              "erts-5.7.5/doc",
              "erts-5.7.5/man",
              "misc"):
        pisitools.removeDir("/usr/lib/erlang/%s" % d)

    # Relocate doc files
    pisitools.domove("/usr/lib/erlang/doc/*", "/usr/share/doc/%s" % get.srcNAME())
    pisitools.removeDir("/usr/lib/erlang/doc")

    for module in shelltools.ls("%s/usr/lib/erlang/erts-*/doc" % get.installDIR()):
        pisitools.domove(os.path.join(module.split(get.installDIR())[-1], "*"),
                         "/usr/share/doc/%s/%s" % (get.srcNAME(), module.split("/")[-2]))

    for lib in shelltools.ls("%s/usr/lib/erlang/lib/*/doc" % get.installDIR()):
        path = os.path.join(lib.split(get.installDIR())[-1])
        pisitools.domove("%s/*" % path, "/usr/share/doc/%s/%s" % (get.srcNAME(), lib.split("/")[-2]))
        if len(shelltools.ls(path)) == 0:
            pisitools.removeDir(path)

    # Remove dummy installed pdf files
    shelltools.system("./genpdf clean %s/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))

    pisitools.dodoc("EPLICENCE", "AUTHORS")

