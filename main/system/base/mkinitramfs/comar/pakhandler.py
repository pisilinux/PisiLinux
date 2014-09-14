# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess

def generate_initramfs(filepath):
    patterns = ("lib/initramfs", "boot/kernel", "bin/busybox")
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith(patterns):
            for kernel in os.listdir("/etc/kernel"):
                subprocess.call(["/sbin/mkinitramfs", "--type", kernel])
            return

def setupPackage(metapath, filepath):
    generate_initramfs(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    generate_initramfs(filepath)
