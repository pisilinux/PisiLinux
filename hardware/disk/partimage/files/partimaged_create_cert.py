#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
import re
from sys import exit, stderr
import locale
from subprocess import call

class unencprivkey:
    cmd = ["/usr/bin/openssl", "genrsa", "-out", "/etc/partimaged/partimaged.key", "1024"]
    path = "/etc/partimaged/partimaged.key"
    name = "Private key"

class certreq:
    cmd = ["/usr/bin/openssl", "req", "-new", "-x509", "-outform", "PEM", "-out", "/etc/partimaged/partimaged.csr", "-key", "/etc/partimaged/partimaged.key", "-config", "/etc/partimaged/servercert.cnf"]
    path = "/etc/partimaged/partimaged.csr"
    name = "Certificate request"

class selfsigncert:
    cmd = ["/usr/bin/openssl", "x509", "-in", "/etc/partimaged/partimaged.csr", "-out", "/etc/partimaged/partimaged.cert", "-signkey", "/etc/partimaged/partimaged.key"]
    path = "/etc/partimaged/partimaged.cert"
    name = "Self-signed certifcate"

warningmsg = "\nThis script will create secure key for partimaged.\nPlease customize the file /etc/partimaged/servercert.cnf before continuing!\n"

yesexpr = re.compile(locale.nl_langinfo(locale.YESEXPR))
print warningmsg
prompt = "continue? (yes/no): "
s = raw_input(prompt.encode('utf-8'))

if yesexpr.search(s) == None:
    print "Aborted."
    exit()

sections = [unencprivkey, certreq, selfsigncert]

for section in sections:

    print "Generating %s:" % section.name

    if os.path.isfile(section.path):
        print "\nError: %s already exists: %s" % (section.name, section.path)
        exit()

    try:
        retcode = call(section.cmd)
        if retcode < 0:
            print >>sys.stderr, "Error, child was terminated by signal", -retcode
            exit()
        else:
            print "done.\n"
    except OSError, e:
        print >>sys.stderr, "Execution failed:", e
        exit()

os.chmod("/etc/partimaged/partimaged.key", 0600)
os.chown("/etc/partimaged/partimaged.key", 134, 0)
os.chmod("/etc/partimaged/partimaged.cert", 0644)
os.chmod("/etc/partimaged/partimaged.csr", 0644)
os.chown("/etc/partimaged/partimaged.cert", 0, 0)
os.chown("/etc/partimaged/partimaged.csr", 0, 0)