#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

NGINX_HOME = '/var/lib/nginx'
NGINX_PID  = '/run/nginx.pid'
NGINX_LOCK = '/run/nginx.lock'
NGINX_CONF = '/etc/nginx/nginx.conf'
NGINX_HTML = '/var/www/nginx'

LOG_DIR    = '/var/log/nginx'
ERROR_LOG    = '%s/error.log' % LOG_DIR
ACCESS_LOG   = '%s/access.log' % LOG_DIR

def setup():
    autotools.rawConfigure("--user=nginx \
                            --group=nginx \
                            --prefix=%(html)s \
                            --sbin-path=/usr/sbin/nginx \
                            --conf-path=%(conf)s \
                            --pid-path=%(pid)s \
                            --lock-path=%(lock)s \
                            --error-log-path=%(error)s \
                            --http-log-path=%(access)s \
                            --http-client-body-temp-path=%(home)s/client_body \
                            --http-proxy-temp-path=%(home)s/proxy \
                            --http-fastcgi-temp-path=%(home)s/fastcgi \
                            --with-ipv6 \
                            --with-http_ssl_module \
                            --with-http_realip_module \
                            --with-http_addition_module \
                            --with-http_xslt_module \
                            --with-http_image_filter_module \
                            --with-http_geoip_module \
                            --with-http_sub_module \
                            --with-http_dav_module \
                            --with-http_flv_module \
                            --with-http_gzip_static_module \
                            --with-http_stub_status_module \
                            --with-http_perl_module \
                            --with-mail \
                            --with-mail_ssl_module" % {'html': NGINX_HTML, \
                                                       'conf': NGINX_CONF, \
                                                       'pid': NGINX_PID, \
                                                       'lock': NGINX_LOCK, \
                                                       'error': ERROR_LOG, \
                                                       'access': ACCESS_LOG, \
                                                       'home': NGINX_HOME})


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # For 3rd-party configuration files
    pisitools.dodir("/etc/nginx/conf.d")

    # Remove empty dir
    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())

    # Add log dir and touch them :) Nginx needs pre-defined *.log files
    pisitools.dodir(LOG_DIR)
    shelltools.touch("%s%s" % (get.installDIR(), ERROR_LOG))
    shelltools.touch("%s%s" % (get.installDIR(), ACCESS_LOG))

    pisitools.dodir(NGINX_HOME + "/client_body")
    pisitools.dodir(NGINX_HOME + "/fastcgi")
    pisitools.dodir(NGINX_HOME + "/proxy")

    pisitools.remove("/usr/lib/perl5/site_perl/*/*/*/*/.packlist")

    pisitools.dodoc("README", "LICENSE")
