from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Postfix Mail Server",
                 "tr": "Postfix E-Posta Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/postfix",
                 args="start",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/postfix",
                args="stop",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/postfix",
                args="reload")

def status():
    return isServiceRunning(command="/usr/lib/postfix/master")
