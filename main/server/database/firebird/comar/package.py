#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, pwd, socket

pid_dir = "/run/firebird"
log_file = "/var/log/firebird.log"

uid = pwd.getpwnam("firebird")[2]
hostname = socket.gethostname()

def touch(filename):
    try:
        f = open(filename, "w")
        f.close()
    except IOError:
        fail("Failed to create %s file" % filename)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
#    # Configure PID directory
    os.chown(pid_dir, uid, -1)

    # Create log file
    touch(log_file)
    os.chown(log_file, uid, -1)
    os.chmod(log_file, 0644)

    # Configure security2.fdb file
    os.chown("/opt/firebird/security2.fdb", uid, -1)

    # Create lock files
    for lock_filename in ("isc_guard1", "isc_init1", "isc_lock1"):
        lock_filename = "/opt/firebird/%s.%s" % (lock_filename, hostname)
        touch(lock_filename)
        os.chown(lock_filename, uid, -1)
        os.chmod(lock_filename, 0644)

def preRemove():
    # Remove lock files
    for lock_filename in ("isc_guard1", "isc_init1", "isc_lock1"):
        lock_filename = "/opt/firebird/%s.%s" % (lock_filename, hostname)
        if os.path.exists(lock_filename):
            os.remove(lock_filename)
