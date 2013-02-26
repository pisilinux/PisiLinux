#/usr/bin/python

import os

permissions = {
                "/etc/sudoers"          :   ["0440", "root:root"],
                "/etc/sudoers.d"        :   ["0750", "root:root"],
                "/var/db/sudo"          :   ["0700", "root:root"],
                "/usr/bin/sudo"         :   ["4111", "root:root"],
                "/usr/bin/sudoedit"     :   ["4111", "root:root"],
                "/usr/bin/sudoreplay"   :   ["0111", "root:root"],
            }


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for _file, perms in permissions.items():
        # The list above is general, some paths may not exist depending on the configuration
        if os.path.exists(_file):
            os.system("/bin/chown -R %s %s" % (perms[1], _file))
            os.system("/bin/chmod %s %s" % (perms[0], _file))
