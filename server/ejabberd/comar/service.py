from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "ejabberd Jabber Server",
                 "tr": "ejabberd Jabber Sunucusu"})

@synchronized
def start():
    # Delete the old cookie, it's in spool dir
    cookie_file = "/var/lib/ejabberd/.erlang.cookie"
    if os.path.exists(cookie_file):
        os.unlink(cookie_file)

    config_file = config.get("CONFIG_FILE", "/etc/ejabberd/ejabberd.cfg")
    ulimit_max_files = config.get("ULIMIT_MAX_FILES", "1024")

    # System default is 1024 so set this if ulimit_max_files != 1024
    if ulimit_max_files != "1024":
        os.system("ulimit -n %s" % ulimit_max_files)

    # Start the node
    args=" ".join(["start",
                   "--config %s" % config_file,
                   "--ctl-config /etc/ejabberd/ejabberdctl.cfg",
                   "--logs \"/var/log/ejabberd\"",
                   "--spool \"/var/lib/ejabberd/spool\""])

    startService(command="/usr/sbin/ejabberdctl",
                 args=args)

    # It takes some time to actually start necessary nodes
    time.sleep(5)

@synchronized
def stop():
    stopService(command="/usr/sbin/ejabberdctl",
        args="stop",
        donotify=False)

    # It takes some time to actually stop necessary nodes
    time.sleep(5)

def status():
    return run("/usr/sbin/ejabberdctl status") == 0
