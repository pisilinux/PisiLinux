from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "OpenLDAP Server",
                 "tr": "OpenLDAP Sunucusu"})
serviceConf = "slapd"

def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"

    startService(command="/usr/libexec/slapd",
                 args="-u ldap -g ldap %s" % config.get("OPTS", ""),
                 pidfile="/var/run/openldap/slapd.pid",
                 donotify=True)

def stop():
    stopService(pidfile="/var/run/openldap/slapd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/openldap/slapd.pid")
