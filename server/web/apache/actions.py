#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "httpd-%s" % get.srcVERSION()

def config_layout():
    return """
<Layout PisiLinux>
    prefix:          /usr
    exec_prefix:     /usr
    bindir:          /usr/bin
    sbindir:         /usr/sbin
    libdir:          /usr/lib
    libexecdir:      /usr/lib/apache2/modules
    mandir:          /usr/share/man
    infodir:         /usr/share/info
    includedir:      /usr/include/apache2
    installbuilddir: /usr/lib/apache2/build
    datadir:         /var/www/localhost
    errordir:        /var/www/localhost/error
    iconsdir:        /var/www/localhost/icons
    htdocsdir:       /var/www/localhost/htdocs
    cgidir:          /var/www/localhost/cgi-bin
    manualdir:       /usr/share/doc/version/manual
    sysconfdir:      /etc/apache2
    localstatedir:   /var
    runtimedir:      /run
    logfiledir:      /var/log/apache2
    proxycachedir:   /var/cache/apache2
</Layout>"""

def modules_config():
    disabled = ['bucketeer', 'example', 'optional-fn-export', 'optional-fn-import',
                'optional-hook-export','optional-hook-import']

    static = ['so']

    # auth_ldap, ldap needed
    shared = ['actions', 'alias', 'asis', 'auth_basic', 'authn_dbm', 'authn_file',
              'auth_digest', 'authz_host', 'autoindex', 'cache', 'case_filter',
              'case-filter-in', 'cern-meta', 'cgi', 'cgid', 'charset-lite', 'dav',
              'dav-fs', 'deflate', 'dir', 'disk-cache', 'echo', 'env', 'expires',
              'ext-filter', 'file-cache', 'headers', 'imagemap', 'include', 'info',
              'log_config', 'logio', 'mem-cache', 'mime', 'mime-magic', 'negotiation',
              'proxy', 'proxy-connect','proxy-ftp', 'proxy-http', 'rewrite', 'setenvif',
              'speling', 'status', 'unique-id', 'userdir', 'usertrack', 'vhost-alias']

    conf = ""

    for i in disabled:
        conf += "--disable-%s " % i
    for i in static:
        conf += "--enable-%s=yes " % i
    for i in shared:
        conf += "--enable-%s=shared " % i

    return conf

def setup():
    shelltools.echo("config.layout", config_layout())
    pisitools.dosed("config.layout", "version", get.srcNAME())

    #for d in ["apr","apr-util","pcre"]:
        #shelltools.unlinkDir("srclib/%s" % d)

    # this fixes segfaults, remember omit-frame-pointer will be default soon
    if get.ARCH() == "i686":
        shelltools.export("CFLAGS", "%s -fno-omit-frame-pointer" % get.CFLAGS())
    shelltools.export("LDFLAGS", "-Wl,-z,relro,-z,now")

    autotools.rawConfigure('--with-mpm=prefork \
                            --enable-layout=PisiLinux \
                            --enable-mods-shared=all \
                            --with-ssl=/usr \
                            --enable-ssl=shared \
                            %s \
                            --with-z=/usr \
                            --with-port=80 \
                            --with-program-name=apache2 \
                            --with-apr=/usr/bin/apr-1-config \
                            --with-apr-util=/usr/bin/apu-1-config \
                            --with-suexec-safepath="/usr/bin:/bin" \
                            --with-suexec-logfile=/var/log/apache2/suexec_log \
                            --with-suexec-bin=/usr/sbin/suexec \
                            --with-suexec-userdir="public_html" \
                            --with-suexec-caller=apache \
                            --with-suexec-docroot=/var/www \
                            --with-suexec-uidmin=1000 \
                            --with-suexec-gidmin=100 \
                            --with-suexec-umask=077 \
                            --enable-suexec=shared \
                            --enable-pie \
                            --with-pcre=/usr/bin/pcre-config' % modules_config())

    pisitools.dosed("include/ap_config_auto.h", "apache2\.conf", "httpd.conf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s INSTALL_SUEXEC='setuid'" % get.installDIR())

    pisitools.dosym("/usr/lib", "/usr/lib/apache2/lib")
    pisitools.dosym("/var/log/apache2", "/usr/lib/apache2/logs")
    pisitools.dosym("/etc/apache2", "/usr/lib/apache2/conf")

    pisitools.dosbin("support/split-logfile")
    pisitools.dosbin("support/list_hooks.pl")
    pisitools.dosbin("support/logresolve.pl")
    pisitools.dosbin("support/log_server_status")

    pisitools.dosbin("apache2")

    pisitools.domove("/usr/sbin/envvars*", "/usr/lib/apache2/build")
    pisitools.dosed("%s/usr/bin/apxs" % get.installDIR(), \
                    "my \$envvars = get_vars\(\"bindir\"\) \. \"/envvars\";", \
                    "my $envvars = \"$installbuilddir/envvars\";")

    # Clean-up
    pisitools.remove("/etc/apache2/*")
    pisitools.remove("/var/www/localhost/htdocs/*")

    # Add conf.d for 3rd party configuration files
    pisitools.dodir("/etc/apache2/conf.d")

    # ssl enabled apache needs that one
    pisitools.dodir("/var/cache/apache2")

    # Fix wrong libtool path
    pisitools.dosed("%s/usr/lib/apache2/build/config_vars.mk" % get.installDIR(), \
                    "/usr/lib/apache2/build/libtool", \
                    "/usr/bin/libtool")

    # Remove cgi scripts which are vulnerable, see CVE-2007-4049
    pisitools.remove("/var/www/localhost/cgi-bin/*")


    pisitools.dodoc("ABOUT_APACHE", "CHANGES", "LAYOUT", "LICENSE", "README*")

    pisitools.removeDir("/run")
