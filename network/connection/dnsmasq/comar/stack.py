#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import string
import subprocess
import dnsmasq

HEADER_DEFAULT = """# Default DNS settings
#
"""

HOST_CHARS = string.ascii_letters + string.digits + '.' + '_' + '-'
NAME_PATH = "/etc/env.d/01hostname"
CMD_ENV = "/sbin/update-environment"
HOSTS_PATH = "/etc/hosts"

RESOLV_USER = "/etc/resolv.default.conf"

MSG_ERR_INVLCHRSHSNM = {"en": "Invalid character(s) '%s' found in hostname.",
                        "tr": "Bilgisayar adında geçersiz karakter(ler) ('%s') bulundu.",
                        }

# Network.Stack methods

def getNameServers():
    servers = []
    if not os.access(RESOLV_USER, os.R_OK):
        return servers
    for line in file(RESOLV_USER):
        line = line.strip()
        if line.startswith("nameserver"):
            ip = line.split()[1]
            if ip not in servers:
                servers.append(ip)
    return servers

def setNameServers(nameservers, searchdomain):
    f = file(RESOLV_USER, "w")
    f.write(HEADER_DEFAULT)

    for server in nameservers:
        f.write("nameserver %s\n" % server)

    if searchdomain:
        f.write("searchdomain %s\n" % searchdomain)

    f.close()

def registerNameServers(ifname, nameservers, searchdomain):
    dnsMasq = dnsmasq.DnsMasq()
    for server in nameservers:
        dnsMasq.registerNameServer(ifname, server)
    dnsMasq.clearCache()

def unregisterNameServers(ifname, nameservers, searchdomain):
    dnsMasq = dnsmasq.DnsMasq()
    dnsMasq.unregisterNameServers(ifname)
    dnsMasq.clearCache()

def flushNameCache():
    dnsMasq = dnsmasq.DnsMasq()
    dnsMasq.clearCache()

def getHostName():
    cmd = subprocess.Popen(["/usr/bin/hostname"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    a = cmd.communicate()
    if a[1] == "":
        return a[0].rstrip("\n")
    return ""

def setHostName(hostname):
    if not hostname:
        return
    invalid = filter(lambda x: not x in HOST_CHARS, hostname)
    if len(invalid) > 0:
        fail(_(MSG_ERR_INVLCHRSHSNM) % ("".join(invalid)))

    # hostname
    if os.path.exists(NAME_PATH):
        import re
        f = file(NAME_PATH)
        data = f.read()
        f.close()
        data = re.sub('HOSTNAME="(.*)"', 'HOSTNAME="%s"' % hostname, data)
    else:
        data = 'HOSTNAME="%s"\n' % hostname
    f = file(NAME_PATH, "w")
    f.write(data)
    f.close()

    # hosts
    f = file(HOSTS_PATH)
    data = f.readlines()
    f.close()
    f = file(HOSTS_PATH, "w")
    flag = 1
    for line in data:
        if line.startswith("127.0.0.1"):
            line = "127.0.0.1 localhost %s\n" % hostname
            flag = 0
        f.write(line)
    if flag:
        f.write("127.0.0.1 localhost %s\n" % hostname)
    f.close()

    # update environment
    os.system(CMD_ENV)
