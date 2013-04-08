#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

# Generate the list of files needed in initramfs for plymouth

exclude_list = (
                    "/usr/bin/plymouth-log-viewer",
                    "/usr/sbin/plymouth-set-default-theme",
                    "/usr/lib/plymouth/renderers/x11.so",
                    "/usr/lib/plymouth/label.so",
               )

paths = (
            "/usr/share/plymouth",
            "/usr/share/pixmaps",
            "/etc/plymouth",
        )

FILE_LIST = "lib/initramfs/plymouth.list"

def usage():
    print "%s <directory>" % sys.argv[0]
    return 1

def generate_needed_binary_list():
    binaries = set()
    executables = os.popen("find -type f -executable | cut -c2-").read().strip().split()
    executables = set(executables).difference(exclude_list)

    for exe in executables:
        if exe.endswith(".la"):
            continue
        if ".so." in exe:
            # Add the libfoo.so.X symlink instead of libfoo.so.X.y.z
            symlink = exe.rsplit(".", 2)[0]
            if os.path.exists(symlink[1:]):
                binaries.add(symlink)
                continue

        binaries.add(exe)

    for exe in executables:
        for line in os.popen("ldd %s" % exe[1:]):
            if "=> /" in line:
                binaries.add(line.split()[2])
            elif line.strip().startswith("/"):
                binaries.add(line.strip().split()[0])

    return binaries

def get_other_file_list():
    files = ["usr/share/pixmaps/plymouth-pisilinux.png", "usr/share/themes/charge/charge.plymouth"]
    for path in paths:
        files.extend(os.popen("find %s -type f" % path[1:]).read().strip().split())

    return ["/%s" % f for f in files]

if __name__ == "__main__":

    try:
        directory = sys.argv[1]
    except:
        sys.exit(usage())

    os.chdir(directory)
    files = generate_needed_binary_list()
    files = files.union(get_other_file_list())

    if not os.path.exists(os.path.dirname(FILE_LIST)):
        os.makedirs(os.path.dirname(FILE_LIST))
    open(FILE_LIST, "w").write("\n".join(sorted(files)))
