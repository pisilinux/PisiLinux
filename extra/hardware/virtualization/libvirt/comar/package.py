#/usr/bin/python

import os

permissions = {
                "/etc/libvirt"                          :   ["0700", "root:root"],
                "/etc/libvirt/qemu"                     :   ["0700", "root:root"],
                "/etc/libvirt/nwfilter"                 :   ["0700", "root:root"],
                "/etc/libvirt/qemu/networks"            :   ["0700", "root:root"],
                "/etc/libvirt/qemu/networks/autostart"  :   ["0700", "root:root"],
                "/var/log/libvirt"                      :   ["0700", "root:root"],
                "/var/log/libvirt/qemu"                 :   ["0700", "root:root"],
                "/var/log/libvirt/lxc"                  :   ["0700", "root:root"],
                "/var/log/libvirt/uml"                  :   ["0700", "root:root"],
                "/var/lib/libvirt"                      :   ["0755", "root:root"],
                "/var/lib/libvirt/images"               :   ["0711", "root:root"],
                "/var/lib/libvirt/boot"                 :   ["0711", "root:root"],
                "/var/lib/libvirt/qemu"                 :   ["0750", "qemu:qemu"],
                "/var/lib/libvirt/lxc"                  :   ["0700", "root:root"],
                "/var/lib/libvirt/uml"                  :   ["0700", "root:root"],
                "/var/lib/libvirt/network"              :   ["0700", "root:root"],
                "/var/lib/libvirt/dnsmasq"              :   ["0755", "root:root"],
                "/var/cache/libvirt/qemu"               :   ["0750", "qemu:qemu"],
                "/var/cache/libvirt"                    :   ["0700", "root:root"],
                "/run/libvirt"                      :   ["0755", "root:root"],
                "/run/libvirt/qemu"                 :   ["0700", "qemu:qemu"],
                "/run/libvirt/uml"                  :   ["0700", "root:root"],
                "/usr/libexec/libvirt_proxy"            :   ["4755", "root:root"],
            }


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for _file, perms in permissions.items():
        # The list above is general, some paths may not exist depending on the configuration
        if os.path.exists(_file):
            os.system("/bin/chown -R %s %s" % (perms[1], _file))
            os.system("/bin/chmod %s %s" % (perms[0], _file))
    os.system("groupadd libvirt")
    os.system("usermod -G libvirt %s" % os.getusername())
