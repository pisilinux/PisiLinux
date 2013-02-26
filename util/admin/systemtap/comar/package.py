#/usr/bin/python

import os

LOGFILE = "/var/log/stap-server/log"

permissions = {
                "/usr/share/systemtap/runtime/uprobes"  :   ["0775", "root:stap-server"],
                LOGFILE                                 :   ["0664", "stap-server:stap-server"],
            }

# TODO
# If it does not already exist, as stap-server, generate the certificate
# used for signing and for ssl.
#if test ! -e ~stap-server/.systemtap/ssl/server/stap.cert; then
#   runuser -s /bin/sh - stap-server -c %{_libexecdir}/%{name}/stap-gen-cert >/dev/null
   # Authorize the certificate as a trusted ssl peer and as a trusted signer
   # on the local host.
#   %{_libexecdir}/%{name}/stap-authorize-cert ~stap-server/.systemtap/ssl/server/stap.cert %{_sysconfdir}/systemtap/ssl/client >/dev/null
#   %{_libexecdir}/%{name}/stap-authorize-cert ~stap-server/.systemtap/ssl/server/stap.cert %{_sysconfdir}/systemtap/staprun >/dev/null
#fi

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists(LOGFILE):
        open(LOGFILE, "w").write("")

    for _file, perms in permissions.items():
        # The list above is general, some paths may not exist depending on the configuration
        if os.path.exists(_file):
            os.system("/bin/chown -R %s %s" % (perms[1], _file))
            os.system("/bin/chmod %s %s" % (perms[0], _file))
