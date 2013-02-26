#!/usr/bin/python

import os
import pwd
import grp

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown ldap:ldap /var/lib/openldap-data")
    os.system("/bin/chown ldap:ldap /var/lib/openldap-slurp")
    os.system("/bin/chown ldap:ldap /var/run/openldap")
    os.system("/bin/chown root:ldap /etc/openldap/slapd.conf")
    os.system("/bin/chown root:ldap /etc/openldap/slapd.conf.default")
    os.system("/bin/chmod 0700 /var/lib/openldap-data")
    os.system("/bin/chmod 0700 /var/lib/openldap-slurp")
    os.system("/bin/chmod 0755 /var/run/openldap")
    os.system("/bin/chmod 0640 /etc/openldap/slapd.conf")
    os.system("/bin/chmod 0640 /etc/openldap/slapd.conf.default")
