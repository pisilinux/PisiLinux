# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Secure Shell Server",
                 "tr": "Güvenli Kabuk Sunucusu"
                 })

MSG_ERR_NEEDCONF = _({"en": "You need /etc/ssh/sshd_config to run sshd.",
                      "tr": "Sshd'yi çalıştırabilmek için /etc/ssh/sshd_config'e ihtiyaç var.",
                      })

PID_FILE = "/run/sshd.pid"
RSA1_KEY = "/etc/ssh/ssh_host_key"
RSA_KEY = "/etc/ssh/ssh_host_rsa_key"
DSA_KEY = "/etc/ssh/ssh_host_dsa_key"

def check_config():
    import os
    if not os.path.exists("/etc/ssh/sshd_config"):
        fail(MSG_ERR_NEEDCONF)
    if not os.path.exists(RSA1_KEY):
        # Default is 2048 bits, and is considered sufficient.
        run("/usr/bin/ssh-keygen", "-t", "rsa1",
            "-f", "/etc/ssh/ssh_host_key", "-N", "")
    if not os.path.exists(DSA_KEY):
        run("/usr/bin/ssh-keygen", "-t", "dsa",
            "-f", "/etc/ssh/ssh_host_dsa_key", "-N", "")
    if not os.path.exists(RSA_KEY):
        run("/usr/bin/ssh-keygen", "-t", "rsa",
            "-f", "/etc/ssh/ssh_host_rsa_key", "-N", "")

@synchronized
def start():
    check_config()
    startService(command="/usr/sbin/sshd",
                 pidfile=PID_FILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)

def status():
    return isServiceRunning(PID_FILE)
