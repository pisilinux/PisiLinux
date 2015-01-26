# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

config = """
V                       = 1
CFLAGS                  = %s
LDFLAGS                 = %s
INSTALLDIRS             = vendor
DESTDIR                 = %s
prefix                  = /usr
htmldir                 = /usr/share/doc/git
sysconfdir              = /etc 
ETC_GITCONFIG           = /etc/gitconfig
GITWEB_CSS              = gitweb/gitweb.css
GITWEB_LOGO             = gitweb/git-logo.png
GITWEB_FAVICON          = gitweb/git-favicon.png
GITWEB_JS               = gitweb/gitweb.js
PYTHON_PATH             = /usr/bin/python3 
PERL_MM_OPT             ="" 
GIT_TEST_OPTS           ='--no-color' 
gitwebdir               = /var/www/localhost/cgi-bin
ASCIIDOC8               = 1
ASCIIDOC_NO_ROFF        = 1
BLK_SHA1                = 1
NEEDS_CRYPTO_WITH_SSL   = 1
USE_LIBPCRE             = 1
NO_CROSS_DIRECTORY_HARDLINKS = 1
MAN_BOLD_LITERAL        = 1
V                       = 1 
""" % (get.CFLAGS(), get.LDFLAGS(), get.installDIR())


def setup():
    shelltools.echo("config.mak", config)

def build():
    pisitools.dosed("Makefile", "^CC = .*$", "CC = %s" % get.CC())
    autotools.make("all doc gitweb/gitweb.cgi")

def install():
    autotools.rawInstall("install-doc")

    # Install bash completion
    pisitools.insinto("/etc/bash_completion.d", "contrib/completion/git-completion.bash", "git")
    shelltools.chmod("%s/etc/bash_completion.d/git" % get.installDIR(), 0644)

    # for git-daemon
    pisitools.dodir("/pub/scm")

    # emacs support
    autotools.install("-C contrib/emacs")
    pisitools.insinto("/usr/share/doc/emacs-git", "contrib/emacs/README")

    # Some docs
    pisitools.dodoc("README", "COPYING", "Documentation/SubmittingPatches")

    # remove .pod and .packlist files
    perlmodules.removePodfiles()
    perlmodules.removePacklist()
