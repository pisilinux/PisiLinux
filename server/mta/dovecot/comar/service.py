from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Dovecot POP3/IMAP Server",
                 "tr": "Dovecot POP3/IMAP Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/dovecot",
                 pidfile="/var/run/dovecot/master.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/dovecot/master.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/dovecot/master.pid")
