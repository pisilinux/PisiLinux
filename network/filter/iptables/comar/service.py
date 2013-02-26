#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Firewall",
                 "tr": "Güvenlik Duvarı"})

LOCK_FILE = "/var/lock/subsys/iptables"
FIREWALL_PATH = "/etc/firewall.conf"

import os
import pardus.netfilterutils as iptables
from pardus import iniutils

def writeFile(filename, content="", mode=0600):
    '''Writes content to filename and sets file mode.'''
    file(filename, "w").write(content)
    os.chmod(filename, mode)

def readFile(filename):
    """Return content of a file"""
    return file(filename, "r").read()

def startNetworkFirewall():
    INI = iniutils.iniParser(FIREWALL_PATH)
    try:
        info = INI.getSection("general")
    except iniutils.iniParserError:
        return
    if info.get("state", "off") == "on":
        call(script(), "Network.Firewall", "setState", ("on"))

def stop():
    # Save rules
    writeFile("/var/lib/iptables/rules", iptables.getRules())

    # Clear chains & rules
    iptables.clear()

    # Remove lock file
    if os.access(LOCK_FILE, os.F_OK):
        os.unlink(LOCK_FILE)

    # Notify clients
    notify("System.Service", "Changed", (script(), "stopped"))

def start():
    # Clear chains & rules
    iptables.clear()

    # Load rules
    profile_file = "/var/lib/iptables/rules"
    if os.path.exists(profile_file):
        rules = readFile(profile_file)
        iptables.restoreRules(rules)

    # Create lock file
    writeFile(LOCK_FILE, "")

    # Initialize Network.Firewall, if necessary
    startNetworkFirewall()

    # Notify clients
    notify("System.Service", "Changed", (script(), "started"))

def status():
    return os.access(LOCK_FILE, os.F_OK)
