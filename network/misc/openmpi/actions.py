#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    # Disable test causing sandbox violations
    pisitools.dosed("test/util/Makefile.in", "^(check_PROGRAMS.*?)\sopal_path_nfs\$\(EXEEXT\)", "\\1")

    shelltools.export("LDFLAGS","%s -Wl,-z,noexecstack" % get.LDFLAGS())

    autotools.configure("--enable-pretty-print-stacktrace \
                         --enable-orterun-prefix-by-default \
                         --without-slurm")

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS","LICENSE","README","NEWS")

    pisitools.remove("/usr/include/event2/event_compat.h")
    pisitools.remove("/usr/include/event2/http.h")
    pisitools.remove("/usr/include/event2/thread.h")
    pisitools.remove("/usr/include/event2/rpc.h")
    pisitools.remove("/usr/include/event2/rpc_compat.h")
    pisitools.remove("/usr/include/event2/keyvalq_struct.h")
    pisitools.remove("/usr/include/event2/listener.h")
    pisitools.remove("/usr/include/event2/dns_struct.h")
    pisitools.remove("/usr/include/event2/rpc_struct.h")
    pisitools.remove("/usr/include/event2/bufferevent_ssl.h")
    pisitools.remove("/usr/include/event2/buffer.h")
    pisitools.remove("/usr/include/event2/tag_compat.h")
    pisitools.remove("/usr/include/event2/util.h")
    pisitools.remove("/usr/include/event2/bufferevent_compat.h")
    pisitools.remove("/usr/include/event2/event-config.h")
    pisitools.remove("/usr/include/event2/bufferevent.h")
    pisitools.remove("/usr/include/event2/buffer_compat.h")
    pisitools.remove("/usr/include/event2/http_compat.h")
    pisitools.remove("/usr/include/event2/dns_compat.h")
    pisitools.remove("/usr/include/event2/http_struct.h")
    pisitools.remove("/usr/include/event2/event_struct.h")
    pisitools.remove("/usr/include/event2/dns.h")
    pisitools.remove("/usr/include/event2/event.h")
    pisitools.remove("/usr/include/event2/tag.h")
    pisitools.remove("/usr/include/event2/bufferevent_struct.h")