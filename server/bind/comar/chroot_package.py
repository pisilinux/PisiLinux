#!/usr/bin/python

import os
import stat
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    CHROOT  = "/var/named/chroot"
    NODES   = {
                "/dev/random"    : [stat.S_IFCHR | 0666, 1, 8],
                "/dev/zero"      : [stat.S_IFCHR | 0666, 1, 5],
                "/dev/null"      : [stat.S_IFCHR | 0666, 1, 3],
                "/dev/urandom"   : [stat.S_IFCHR | 0666, 1, 9],
                "/dev/log"       : [stat.S_IFSOCK | 0666, 1, 1],
              }

    # Create device NODES in chroot
    for node, values in NODES.items():
        if not os.path.exists("%s%s" % (CHROOT, node)):
            os.mknod("%s%s" % (CHROOT, node), values[0], os.makedev(values[1], values[2]))

    try:
        os.unlink("%s/etc/localtime" % CHROOT)
    except:
        pass

    # Copy config files to run under chroot
    shutil.copy("/etc/localtime", "%s/etc/localtime" % CHROOT)

    for files in ["/etc/bind/bind.keys", "/etc/bind/named.conf", "/etc/bind/rndc.key", "/var/named/named.ca"]:
        shutil.copy("%s" % files, "%s%s" % (CHROOT, files))

    try:
        shutil.copytree("/var/named/pri", "%s/var/named/pri" % CHROOT)
    except OSError:
        pass

    try:
        shutil.copytree("/var/named/sec", "%s/var/named/sec" % CHROOT)
    except OSError:
        pass

    os.system("ln -s ../../var/named/pri /var/named/chroot/etc/bind/")
    os.system("ln -s ../../var/named/sec /var/named/chroot/etc/bind/")

    # Fix permissions
    os.system("chmod 0700 %s" % CHROOT)
    os.system("chown named:named %s" % CHROOT)
    os.system("chown -R named:named %s/var/named" % CHROOT)
    os.system("chown -R named:named %s/etc/bind" % CHROOT)
    os.system("chown -R named:named %s/var/run/named" % CHROOT)
    os.system("chown -R named:named %s/var/log" % CHROOT)