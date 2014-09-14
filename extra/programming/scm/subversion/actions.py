#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

def setup():
    # Respect the user LDFLAGS
    shelltools.system("./autogen.sh")

    shelltools.export("EXTRA_LDFLAGS", get.LDFLAGS())

    autotools.configure("--disable-static \
                         --with-jdk=/usr/lib/jvm/java-7-openjdk \
                         --enable-javahl \
                         --with-apr=/usr \
                         --with-apr-util=/usr \
                         --with-apache=/usr/lib/apache2/ \
                         --with-apxs \
                         --with-serf=/usr \
                         --with-sqlite=/usr \
                         --with-zlib=/usr \
                         --with-jikes=no \
                         --with-kwallet \
                         --without-berkeley-db \
                         --disable-mod-activation")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    # svn
    autotools.make()

    # python bindings
    autotools.make("swig-py")

    # perl bindings (needed by git-svn*)
    # Sometimes parallel build breaks perl bindings
    autotools.make("-j1 swig-pl")

    # java bindings
    autotools.make("-j1 javahl")

def install():
    # install svn
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install swig-py
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-swig-py")

    # install swig-pl
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-swig-pl")

    # install javahl
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-javahl")

    # Move py/c'into proper dir
    pisitools.domove("/usr/lib/svn-python/svn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/svn-python/libsvn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/svn-python")

    # some helper tools
    pisitools.insinto("/usr/bin", "tools/backup/hot-backup.py", "svn-hot-backup")
    # FIXME: these tools are replaced by new ones
    # pisitools.insinto("/usr/bin", "contrib/client-side/svn_load_dirs.pl", "svn-load-dirs")
    # pisitools.insinto("/usr/bin", "contrib/client-side/svnmerge.py", "svnmerge")
    # shelltools.chmod("%s/usr/bin/svnmerge" % get.installDIR(), 0755)

    # Install upstream bash completion script
    pisitools.insinto("/etc/bash_completion.d", "tools/client-side/bash_completion", "subversion")

    # Documentation and etc.
    #pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "contrib")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "tools/xslt")
    pisitools.insinto("/var/www/localhost/htdocs", "tools/xslt/*")

    # Create virtual repository root
    pisitools.dodir("/var/svn")

    pisitools.dodoc("README")

    # remove unnecessary files i.e. perllocal.pod, .packlist
    perlmodules.removePacklist()
    perlmodules.removePodfiles()
