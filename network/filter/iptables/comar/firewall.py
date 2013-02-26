#!/usr/bin/python
# -*- coding: utf-8 -*-

# i18n

MSG_CONNECTION_NAME = {
    "en": "Internet Sharing",
    "tr": "Internet Paylaşımı",
    "sv": "Internetdelning",
    "fr": "Partage de connexion Internet",
    "es": "Compartir Internet",
    "de": "Internet Freigabe",
    "nl": "Internetverbinding delen",
}

MSG_ALLOWED_PORTS = {
    "en": "Allowed Port Numbers",
    "tr": "İzin Verilen Port Numaraları",
    "sv": "Tillåtna portar",
    "fr": "Numéros de port autorisés",
    "es": "Números de puertos permitidos",
    "de": "Erlaubte Ports",
    "nl": "Toegestane poortnummers",
}

MSG_FORBIDDEN_PORTS = {
    "en": "Forbidden Port Numbers",
    "tr": "İzin Verilmeyen Port Numaraları",
    "sv": "Otillåtna portar",
    "nl": "Verboden poortnummers",
}

MSG_GATEWAY_HOME = {
    "en": "Gate to Home Network",
    "tr": "Ev Ağına Çıkış",
    "sv": "Länk till lokalt nätverk",
    "fr": "Passerelle vers le réseau local",
    "es": "Enlace a la red doméstica",
    "de": "Gateway zum Haus-Netzwerk",
    "nl": "Gateway naar thuisnetwerk",
}

MSG_GATEWAY_INTERNET = {
    "en": "Gate to Internet",
    "tr": "Internet'e Çıkış",
    "sv": "Länk till internet",
    "fr": "Passerelle vers Internet",
    "es": "Enlace a Internet",
    "de": "Gateway zum Internet",
    "nl": "Gateway naar Internet",
}

TITLE_BLOCK_INCOMING = {
    "en": "Block Incoming Connections",
    "tr": "Gelen Bağlantıları Engelle",
    "sv": "Blockera inkommande anslutningar",
    "fr": "Bloquer les connexions entrantes",
    "es": "Bloquear conexiones entrantes",
    "de": "Eingehende Verbindungen blockieren",
    "nl": "Inkomende verbindingen blokkeren",
}
DESCRIPTION_BLOCK_INCOMING = {
    "en": "Blocks all incoming connections to the computer. Exceptions can be set from configuration dialog.",
    "tr": "Bilgisayara gelen tüm bağlantıları engeller. İstisnalar ayarlar penceresinden belirlenebilir.",
    "sv": "Blockerar alla inkommande anslutningar till datorn. Undantag kan läggas till under inställningar.",
    "fr": "Bloque  toute les connexions entrantes dans l'ordinateur. Des exceptions peuvent être définies dans la fenêtre de configuration.",
    "es": "Bloquea todas las conexiones entrantes a la computadora. Se puede especificar excepciones desde el dialogo de configuración.",
    "de": "Blockiert alle eingehenden Verbindungen. Im Konfigurations-Dialog können Ausnahmen angegeben werden.",
    "nl": "Alle inkomende verbindingen naar deze computer blokkeren. Uitzonderingen kunnen in een configuratiedialoog ingesteld worden.",
}

TITLE_BLOCK_OUTGOING = {
    "en": "Block Outgoing Connections",
    "tr": "Giden Bağlantıları Engelle",
    "sv": "Blockera utgående anslutningar",
    "fr": "Bloquer les connexions sortantes",
    "es": "Bloquear conexiones salientes",
    "de": "Ausgehende Verbindungen blockieren",
    "nl": "Uitgaande verbindingen blokkeren",
}
DESCRIPTION_BLOCK_OUTGOING = {
    "en": "Blocks outgoing connections. Forbidden ports can be set from configuration dialog.",
    "tr": "Dışarı yapılan bağlantıları engeller. Yasaklı port numaraları ayarlar penceresinden belirlenebilir.",
    "sv": "Blockerar alla utgående anslutningar till datorn. Undantag kan läggas till under inställningar.",
    "nl": "Uitgaande verbindingen blokkeren. Verboden poorten kunnen in een configuratiedialoog ingesteld worden.",
}

TITLE_INTERNET_SHARING = {
    "en": "Internet Sharing",
    "tr": "Internet Paylaşımı",
    "sv": "Internetdelning",
    "fr": "Partage de connexion Internet",
    "es": "Compartir Internet",
    "de": "Internet Freigabe",
    "nl": "Internetverbinding delen",
}
DESCRIPTION_INTERNET_SHARING = {
    "en": "Allows computers in your local network to connect Internet through this computer.",
    "tr": "Yerel ağınızdaki bilgisayarların, bu bilgisayarı kullanarak Internet'e bağlanmalarını sağlar.",
    "sv": "Låter datorer i det lokala nätverket ansluta till internet via den här datorn.",
    "fr": "Permet aux ordinateurs de votre réseau domestique de se connecter à Internet via cet ordinateur.",
    "es": "Permitir a otros computadoras en su red local acceder a la Internet, a través de ésta computadora",
    "de": "Gibt anderen Computern aus dem lokalen Netzwer die Mäglichkeit, Internet durch diesen Computer hier zu benutzen.",
    "nl": "Geeft andere computers in het lokale netwerk via deze computer toegang tot het internet.",
}


# Don't touch below, if you don't know what you're doing.

# Module configuration settings and templates

FIREWALL_CONF = "/etc/firewall.conf"

IPTABLES_RULES = {
    'filter': [
        '-P INPUT DROP',                        # Default policies
        '-P FORWARD DROP',
        '-P OUTPUT ACCEPT',
        '-N PARDUS-IN',                         # Module container table for INPUT
        '-N PARDUS-IN-MOD-BLOCK',               # Table for BlockIncoming rules
        '-N PARDUS-FW',                         # Module container table for FORWARD
        '-N PARDUS-FW-MOD-SHARING',             # Table for InternetSharingModule rules
        '-N PARDUS-FW-MOD-BLOCK',               # Table for BlockOutgoing rules
        '-N PARDUS-OUT',                        # Module container table for OUTPUT
        '-N PARDUS-OUT-MOD-BLOCK',              # Table for BlockOutgoing rules
        '-A INPUT -i lo -j ACCEPT',             # Accept local
        '-A FORWARD -o lo -j ACCEPT',
        '-A INPUT -m state --state INVALID -j DROP',
        '-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT',
        '-A INPUT -j PARDUS-IN',                # Jump into container tables
        '-A FORWARD -j PARDUS-FW',
        '-A OUTPUT -j PARDUS-OUT',
        '-A PARDUS-IN -j PARDUS-IN-MOD-BLOCK' , # Jump into module tables
        '-A PARDUS-FW -j PARDUS-FW-MOD-BLOCK',
        '-A PARDUS-FW -j PARDUS-FW-MOD-SHARING',
        '-A PARDUS-OUT -j PARDUS-OUT-MOD-BLOCK',
        '-A INPUT -m state --state NEW -j ACCEPT',
    ],
    'nat': [
        '-P PREROUTING ACCEPT',
        '-P POSTROUTING ACCEPT',
        '-P OUTPUT ACCEPT',
        '-N PARDUS-POST',
        '-N PARDUS-POST-MOD-SHARING',
        '-A POSTROUTING -j PARDUS-POST',
        '-A PARDUS-POST -j PARDUS-POST-MOD-SHARING',
    ],
}

DHCPD_CONF = """
ddns-update-style interim;
ignore client-updates;
max-lease-time 500;
default-lease-time 500;
option domain-name-servers 193.140.100.220;
option routers 172.16.0.1;
option subnet-mask 255.255.255.0;
subnet 172.16.0.0 netmask 255.255.255.0 {
    range 172.16.0.2 172.16.0.254;
}
"""

# Utils

import os
import subprocess

from pardus import iniutils
from pardus import netutils
from pardus import netfilterutils

INI = iniutils.iniParser(FIREWALL_CONF)

def listModuleConfigs():
    """
        Returns a list of modules that are configured.
    """
    try:
        modules = INI.listSections()
    except iniutils.iniParserError:
        return
    if "general" in modules:
        modules.remove("general")
    return modules

class ModuleConfig:
    """
        Module configuration parser.
    """
    def __init__(self, name):
        self.name = name
        try:
            self.info = INI.getSection(name)
        except iniutils.iniParserError:
            self.info = {}

    def delete(self):
        INI.removeSection(self.name)

    def save(self):
        is_new = self.name not in listModuleConfigs()
        INI.setSection(self.name, self.info)

def getServiceState(package):
    """
        Returns state of a service.
    """
    return call(package, "System.Service", "info")[2] in ["on", "started"]

def stopService(package, permanent=False):
    """
        Stops a service.
    """
    call(package, "System.Service", "stop")
    if permanent:
        call(package, "System.Service", "setState", ("off"))

def startService(package, restart=False, auto_start=False):
    """
        Starts a service.
    """
    if restart:
        stopService(package)
    if not getServiceState(package):
        call(package, "System.Service", "start")
    if auto_start:
        call(package, "System.Service", "setState", ("on"))

def initializeIPTables():
    """
        Initializes IPTables.
    """
    # Active rules
    rules_active = netfilterutils.parseConf(netfilterutils.getRules())

    # Compare rules
    for chain, rules in IPTABLES_RULES.iteritems():
        if chain not in rules_active or len(set(rules) - set(rules_active[chain])):
            # At least one different rule, need re-initialization
            netfilterutils.clear()
            conf = netfilterutils.makeConf(IPTABLES_RULES)
            netfilterutils.restoreRules(conf)
            break

def execRule(rule):
    """
        Executes IPTables rule
    """
    rule = rule.split()
    rule.insert(0, "/sbin/iptables")
    subprocess.call(rule)

def createConnection(package, device):
    import comar
    link = comar.Link()
    connection = _(MSG_CONNECTION_NAME)
    link.Network.Link[package].setDevice(connection, device)
    link.Network.Link[package].setAddress(connection, "manual", "172.16.0.1", "255.255.255.0", "")
    return connection

def findOrCreateConnection(link, device):
    o_package, o_connecion = None, None
    for package in link.Network.Link:
        if device in link.Network.Link[package].deviceList():
            for connection in link.Network.Link[package].connections():
                info = link.Network.Link[package].connectionInfo(connection)
                if info.get("net_address", "") == "172.16.0.1":
                    return package, connection
            return package, createConnection(package, device)

def makeDHCPConf(interface):
    file("/etc/dhcp/dhcpd.conf", "w").write(DHCPD_CONF)
    file("/etc/conf.d/dhcpd", "w").write("DHCPD_IFACE=%s" % interface)

# Modules

class BlockIncoming:
    def __init__(self):
        self.parametersLast = {}

    def getInfo(self):
        title = _(TITLE_BLOCK_INCOMING)
        description = _(DESCRIPTION_BLOCK_INCOMING)
        icon = "network-server"
        return (title, description, icon)

    def getParameters(self):
        parameters = [
            ("port_exceptions", _(MSG_ALLOWED_PORTS), "editlist", {"format": "[0-9\-]+"}),
        ]
        return parameters

    def checkModule(self, parameters={}, quiet=False):
        pass

    def loadModule(self, parameters={}):
        # Initialize IPTables
        initializeIPTables()
        # Flush rules
        self.unloadModule()
        # Load rules
        for port in parameters.get("port_exceptions", "").split():
            if "-" in port:
                port = port.replace("-", ":")
            execRule("-A PARDUS-IN-MOD-BLOCK -p tcp -m multiport --dports %s -j ACCEPT" % port)
            execRule("-A PARDUS-IN-MOD-BLOCK -p udp -m multiport --dports %s -j ACCEPT" % port)
        # Block else...
        execRule("-A PARDUS-IN-MOD-BLOCK -p tcp -m multiport --dports 0:1024 -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REJECT --reject-with icmp-port-unreachable")
        execRule("-A PARDUS-IN-MOD-BLOCK -p udp -m multiport --dports 0:1024 -j REJECT --reject-with icmp-port-unreachable")
        execRule("-A PARDUS-IN-MOD-BLOCK -j REJECT --reject-with icmp-host-prohibited")

    def unloadModule(self, shutdown=False):
        if not shutdown:
            # Unload rules
            execRule("-F PARDUS-IN-MOD-BLOCK")


class BlockOutgoing:
    def __init__(self):
        self.parametersLast = {}

    def getInfo(self):
        title = _(TITLE_BLOCK_OUTGOING)
        description = _(DESCRIPTION_BLOCK_OUTGOING)
        icon = "security-medium"
        return (title, description, icon)

    def getParameters(self):
        parameters = [
            ("port_exceptions", _(MSG_FORBIDDEN_PORTS), "editlist", {"format": "[0-9\-]+"}),
        ]
        return parameters

    def checkModule(self, parameters={}, quiet=False):
        pass

    def loadModule(self, parameters={}):
        # Initialize IPTables
        initializeIPTables()
        # Flush rules
        self.unloadModule()
        # Load rules
        for port in parameters.get("port_exceptions", "").split():
            if "-" in port:
                port = port.replace("-", ":")
            execRule("-A PARDUS-OUT-MOD-BLOCK -p tcp -m multiport --dports %s -j DROP" % port)
            execRule("-A PARDUS-OUT-MOD-BLOCK -p udp -m multiport --dports %s -j DROP" % port)
            execRule("-A PARDUS-FW-MOD-BLOCK -p tcp -m multiport --dports %s -j DROP" % port)
            execRule("-A PARDUS-FW-MOD-BLOCK -p udp -m multiport --dports %s -j DROP" % port)

    def unloadModule(self, shutdown=False):
        if not shutdown:
            # Unload rules
            execRule("-F PARDUS-OUT-MOD-BLOCK")
            execRule("-F PARDUS-FW-MOD-BLOCK")


class InternetSharingModule:
    def __init__(self):
        self.parametersLast = {}

    def getInfo(self):
        title = _(TITLE_INTERNET_SHARING)
        description = _(DESCRIPTION_INTERNET_SHARING)
        icon = "network-workgroup"
        return (title, description, icon)

    def getParameters(self):
        def findInterfaces(wireless=True):
            ifaces = []
            for iface in netutils.interfaces():
                if iface.name.startswith("lo") or iface.name.startswith("pan"):
                    continue
                if not wireless and iface.isWireless():
                    continue
                if iface.isEthernet():
                    dev_id = iface.deviceUID()
                    dev_name = netutils.deviceName(iface.deviceUID())
                    if " - " in dev_name:
                        dev_name = dev_name.split(" - ")[1]
                    ifaces.append("%s\t%s" % (dev_id, dev_name))
            return ifaces
        options_in = {
            "choose": "\n".join(findInterfaces())
        }
        options_out = {
            "choose": "\n".join(findInterfaces(wireless=False))
        }
        parameters = [
            ("device-input", _(MSG_GATEWAY_INTERNET), "combo", options_in),
            ("device-output", _(MSG_GATEWAY_HOME), "combo", options_out),
        ]
        return parameters

    def checkModule(self, parameters={}, quiet=False):
        pass

    def loadModule(self, parameters={}):
        # Initialize IPTables
        initializeIPTables()
        # Flush rules
        self.unloadModule()
        # Enable forwarding
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_dynaddr")
        # Load rules
        input = parameters.get("device-input", "")
        output = parameters.get("device-output", "")
        if input and output and input != output:
            in_name = input.split("_")[-1]
            out_name = output.split("_")[-1]
            execRule("-A PARDUS-FW-MOD-SHARING -i %s -o %s -m state --state ESTABLISHED,RELATED -j ACCEPT" % (in_name, out_name))
            execRule("-A PARDUS-FW-MOD-SHARING -i %s -o %s -j ACCEPT" % (out_name, in_name))
            execRule("-t nat -A PARDUS-POST-MOD-SHARING -o %s -j MASQUERADE" % in_name)
            # Create local NAT profile
            import comar
            link = comar.Link()
            package, connection = findOrCreateConnection(link, output)
            link.Network.Link[package].setState(connection, "up")
            # Configure DHCP
            makeDHCPConf(out_name)
            # Start DHCP
            startService("dhcpd", restart=True)

    def unloadModule(self, shutdown=False):
        # Stop DHCP
        stopService("dhcpd")
        if not shutdown:
            # Unload rules
            execRule("-F PARDUS-FW-MOD-SHARING")
            execRule("-P PARDUS-FW-MOD-SHARING ACCEPT")
            execRule("-t nat -F PARDUS-POST-MOD-SHARING")


# Usable modules
MODULES = {
    "internet_sharing": InternetSharingModule,
    "block_incoming": BlockIncoming,
    "block_outgoing": BlockOutgoing,
}

# Network.Firewall model

def listModules():
    return MODULES.keys()

def moduleInfo(module):
    inst = MODULES[module]()
    return inst.getInfo()

def moduleParameters(module):
    inst = MODULES[module]()
    return inst.getParameters()

def getModuleState(module):
    info = ModuleConfig(module).info
    return info.get("state", "off")

def setModuleState(name, state):
    if state in ["on", "off"]:
        # Save state
        module = ModuleConfig(name)
        module.info["state"] = state
        module.save()
        # Execute module if firewall is active
        if getState() == "on":
            inst = MODULES[name]()
            if state == "on":
                inst.loadModule(getModuleParameters(name))
            else:
                inst.unloadModule()
        # Notify clients
        notify("Network.Firewall", "moduleStateChanged", (name, state))

def getModuleParameters(module):
    info = ModuleConfig(module).info
    return info

def setModuleParameters(name, parameters):
    # Save module parameters
    module = ModuleConfig(name)
    for key, value in parameters.iteritems():
        module.info[key] = value
    module.save()
    # Execute module if it's active
    if getState() == "on" and getModuleState(name) == "on":
        inst = MODULES[name]()
        inst.checkModule(parameters)
        inst.loadModule(parameters)
    # Notify clients
    notify("Network.Firewall", "moduleSettingsChanged", (name))

def getState():
    state = ModuleConfig("general").info.get("state", "off")
    if state not in ["on", "off"] or not getServiceState(script()):
        return "off"
    return state

def setState(state):
    if state in ["on", "off"]:
        # Save state
        general = ModuleConfig("general")
        general.info["state"] = state
        general.save()
        if state == "on":
            # Start IPTables
            startService(script(), auto_start=True)
            # Execute active modules
            for module in listModuleConfigs():
                if module not in MODULES:
                    continue
                info = ModuleConfig(module).info
                if info.get("state", "off") == "on":
                    inst = MODULES[module]()
                    inst.loadModule(getModuleParameters(module))
        else:
            # Flush IPTables since every module depends on it
            netfilterutils.clear()
            # Stop IPTables
            stopService(script(), permanent=True)
            # Unload modules
            for module in listModuleConfigs():
                if module not in MODULES:
                    continue
                inst = MODULES[module]()
                inst.unloadModule(shutdown=True)
        # Notify clients
        notify("Network.Firewall", "stateChanged", (state))
