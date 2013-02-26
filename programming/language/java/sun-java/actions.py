#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.util import run_batch, check_file_hash, Error

WorkDir = get.ARCH()
NoStrip = "/"
Name = "7u%s" % get.srcVERSION().split("p")[1]
Arch = "x64" if get.ARCH() == "x86_64" else "i586"
Archive = "jdk-%s-linux-%s.tar.gz" % (Name, Arch)
Url = "http://download.oracle.com/otn-pub/java/jdk/%s-b21/%s" % (Name, Archive)
def setup():
    if not shelltools.isFile(Archive):
        shelltools.system('/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %s %s  --header "Cookie:oraclelicensejdk-%s-oth-JPR=accept-securebackup-cookie;gpw_e24=http://edelivery.oracle.com"' % (Archive, Url, Name))
    hash = run_batch("cat %s.sha1" % Arch)[1].split()[0]
    if not check_file_hash(Archive, hash): raise Error("Wrong sha1sum.")
    shelltools.system("tar -xzf %s" % Archive)

def install():
    for d in shelltools.ls("."):
        if shelltools.isDirectory(d) and d.startswith("jdk"):
            shelltools.cd(d)
            break

    for d in ("bin", "db", "include", "lib", "man"):
        pisitools.insinto("/opt/sun-jdk", "%s" %d)

    pisitools.insinto("/opt/sun-jre", "jre/*")
    pisitools.dosym("../sun-jre", "/opt/sun-jdk/jre")

    pisitools.dodoc("COPYRIGHT", "LICENSE", "*README*")
    path = "%s/opt/sun-jre"
    for f in shelltools.ls(path): 
        if isFile(f): shelltools.unlink(f)

    pisitools.dodir("/usr/lib/browser-plugins")
    pisitools.dosym("/opt/sun-jre/lib/%s/libnpjp2.so" % Arch.replace("i586", "i386").replace("x", "amd"), "/usr/lib/browser-plugins/javaplugin.so")
    pisitools.dosym("/opt/sun-jdk/bin/javah", "/usr/bin/javah")
    pisitools.dosym("/opt/sun-jdk/bin/jar", "/usr/bin/jar")
