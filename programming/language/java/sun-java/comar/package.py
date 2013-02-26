#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

        # Create files used as storage for system preferences.
        PREFS_LOCATION = "/opt/sun-jdk/jre"

        try:
            os.makedirs("%s/.systemPrefs" % PREFS_LOCATION, 0755)
        except OSError:
            pass

        if not os.path.exists("%s/.systemPrefs/.system.lock" % PREFS_LOCATION):
                os.system("/bin/touch %s/.systemPrefs/.system.lock" % PREFS_LOCATION)
                os.system("/bin/chmod 644 %s/.systemPrefs/.system.lock" % PREFS_LOCATION)

        if not os.path.exists("%s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION):
                os.system("/bin/touch %s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION)
                os.system("/bin/chmod 644 %s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION)

        # we fixed this directory permission issue on release 22
        # do not apply chmod for releases greater than 22
        if fromRelease and int(fromRelease) < 22:
            # ensure that directory permissions are OK. See #12209
            perm_fixes = (
                ("/opt/sun-jdk/jre", 0755),
                ("/opt/sun-jdk/jre/.systemPrefs", 0755),
                ("/opt/sun-jdk/jre/man/ja_JP.eucJP", 0755),
            )

            for path, mode in perm_fixes:
                if os.path.exists(path):
                    os.chmod(path, mode)
