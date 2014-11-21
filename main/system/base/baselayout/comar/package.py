#!/usr/bin/python

import os
import grp
import pwd
import shutil

import libuser

### Helper methods

def hav(method, *args):
    try:
        call("baselayout", "User.Manager", method, args)
    except:
        pass

def deleteGroup(group):
    try:
        gid = grp.getgrnam(group)[2]
        # deleteGroup(gid)
        hav("deleteGroup", gid)
    except KeyError:
        pass

def deleteUser(user):
    try:
        uid = pwd.getpwnam(user)[2]
        # deleteUser(uid, delete_files)
        hav("deleteUser", uid, False)
    except KeyError:
        pass

def setGroupId(group_name, gid):
    ctx = libuser.admin()
    group = ctx.lookupGroupByName(group_name)
    if group:
        group.set(libuser.GIDNUMBER, [gid])
        ctx.modifyGroup(group)

def setUserId(user_name, uid):
    ctx = libuser.admin()
    user = ctx.lookupUserByName(user_name)
    if user:
        user.set(libuser.UIDNUMBER, [uid])
        ctx.modifyUser(user)

def migrateUsers():
    # build user -> group map for migration (hopefully we'll drop this in 2012)
    migration = []
    migrationMap = {
                    "removable"     : ["cdrom", "plugdev"],
                    "pnp"           : ["lp", "floppy"],
                    "pnpadmin"      : ["lpadmin"],
                   }
    for user in pwd.getpwall():
        groups = set()
        if 1000 <= user.pw_uid < 65534:
            for group in grp.getgrall():
                if user.pw_name in group.gr_mem:
                    groups.add(group.gr_name)

            for oldGroup, newGroups in migrationMap.items():
                if oldGroup in groups:
                    #groups.remove(oldGroup)
                    groups.update(newGroups)

            if groups:
                migration.append((user.pw_uid, list(groups)))

    # Migrate regular user groups
    for user, group in migration:
        # setUser(uid, realname, homedir, shell, passwd, groups)
        hav("setUser", user, "", "", "", "", group)

# Big ugly zemberek-openoffice hack
def zemberek_hack():
    import re

    f = "/var/db/comar3/scripts/System.Package/zemberek_openoffice.py"

    if os.path.exists(f):
        postContent = open(f).read()
        pattern = re.compile('oxt"\)\[0\]$', re.M)
        postContent = re.sub(pattern, 'oxt")', postContent)
        postContent = re.sub("raise Exception", "print", postContent)
        postFile = open(f, 'w')
        postFile.write(postContent)


### COMAR methods


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # We don't want to overwrite an existing file during upgrade
    specialFiles = ["passwd", "shadow", "group", "fstab", "hosts", "ld.so.conf", "resolv.conf"]

    for specialFile in specialFiles:
        if not os.path.exists("/etc/%s" % specialFile):
            shutil.copy("/usr/share/baselayout/%s" % specialFile, "/etc")

    shutil.copy("/etc/passwd", "/usr/share/baselayout/passwd.backup")
    shutil.copy("/etc/group", "/usr/share/baselayout/group.backup")

    if fromRelease and int(fromRelease) < 143:
        # Release 143 starts using /etc/ld.so.conf.d. Copy ld.so.conf
        # for "include" statement.
        shutil.copy("/usr/share/baselayout/ld.so.conf", "/etc")

    ##################################
    # Merge new system groups
    # addGroup(gid, name)
    groups = (
                (7,   "lp"),
                (11,  "cdrom"),
                (14,  "lpadmin"),
                (19,  "floppy"),
                (20,  "dialout"),
                (22,  "sshd"),
                (30,  "squid"),
                (32,  "rpc"),
                #(46,  "plugdev"),
                (50,  "named"),
                # For systemd/var-lock.mount
                (54,  "lock"),
                (60,  "mysql"),
                (70,  "postgres"),
                (80,  "apache"),
                (90,  "dovecot"),
                (100, "users"),
                (102, "hal"),
                (103, "polkitd"),
                (104, "postfix"),
                (105, "postdrop"),
                (106, "smmsp"),
                (107, "locate"),
                (108, "utmp"),
                (109, "firebird"),
                (110, "dhcp"),
                (111, "ldap"),
                (112, "clamav"),
                (113, "ntlmaps"),
                (116, "colord"),
                (120, "avahi"),
                (121, "avahi-autoipd"),
                (123, "ntp"),
                (124, "gdm"),
                (130, "tss"),
                (131, "ejabberd"),
                (132, "tomcat"),
                (133, "ups"),
                (134, "partimag"),
                (135, "radiusd"),
                (136, "oprofile"),
                (137, "mediatomb"),
                # 'pulse' is for system wide PA daemon.
                (138, "pulse"),
                # In order to access to a system wide PA daemon,
                # a user should be a member of the 'pulse-access' group.
                (139, "pulse-access"),
                (141, "italc"),
                (142, "quassel"),
                (143, "bitlbee"),
                (144, "icecast"),
                (145, "virt"),
                (995, "vboxusers"),
                # Gnokii system user for the SMS daemon
                (146, "gnokii"),
                (150, "svn"),
                (151, "memcached"),
                (152, "rtkit"),
                # NetworkManager user for OpenConnect VPN helper
                (153, "nm-openconnect"),
                (160, "usbmuxd"),
                (161, "openvpn"),
                (162, "privoxy"),
                (163, "kvm"),
                (164, "qemu"),
                (165, "kdm"),
                (166, "polipo"),
                (167, "nginx"),
                (168, "guests"),
                (169, "ntop"),
                # COMAR profile groups
                (200, "pnp"),
                (201, "removable"),
                (204, "power"),
                (205, "pnpadmin"),
                # for RT jackaudio
                (206, "jackuser"),
                (207, "wireshark"),
                (209, "vdr"),
                (210, "ecryptfs"),
                (211, "slocate"),
                (212, "dansguardian"),
            )

    for gid, groupName in groups:
        try:
            group = grp.getgrnam(groupName)
        except KeyError:
            hav("addGroup", gid, groupName)
        else:
            if group.gr_gid != gid:
                setGroupId(groupName, gid)


    ##################################
    # Merge new system users
    # addUser(uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths)

    users = (
                (4,   "lp", "CUPS user", "/var/spool/cups", "/sbin/nologin", "", ["lp"], [], []),
                (15,  "lpadmin", "CUPS administrator", "/var/spool/cups", "/sbin/nologin", "", ["lpadmin"], [], []),
                (20,  "dialout", "Dialout", "/dev/null", "/bin/false", "", ["dialout"], [], []),
                (22,  "sshd", "Privilege-separated SSH", "/var/empty/sshd", "/sbin/nologin", "", ["sshd"], [], []),
                (30,  "squid", "Squid", "/var/cache/squid", "/bin/false", "", ["squid"], [], []),
                (32,  "rpc", "Rpcbind daemon", "/var/lib/rpcbind", "/sbin/nologin", "", ["rpc"], [], []),
                (40,  "named", "Bind", "/var/named", "/bin/false", "", ["named"], [], []),
                (60,  "mysql", "MySQL", "/var/lib/mysql", "/bin/false", "", ["mysql"], [], []),
                (70,  "postgres", "PostgreSQL", "/var/lib/postgresql", "/bin/false", "", ["postgres"], [], []),
                (80,  "apache", "Apache", "/dev/null", "/bin/false", "", ["apache", "svn"], [], []),
                (90,  "dovecot", "Dovecot", "/dev/null", "/bin/false", "", ["dovecot"], [], []),
                (102, "hal", "HAL", "/dev/null", "/bin/false", "", ["hal"], [], []),
                (103, "polkitd", "PolicyKit", "/var/lib/polkit-1", "/bin/false", "", ["polkitd"], [], []),
                (104, "postfix", "Postfix", "/var/spool/postfix", "/bin/false", "", ["postfix"], [], []),
                (106, "smmsp", "smmsp", "/var/spool/mqueue", "/bin/false", "", ["smmsp"], [], []),
                (107, "colord", "colord colour management daemon", "/var/lib/colord", "/bin/false", "", ["colord"], [], []),
                (109, "firebird", "Firebird", "/opt/firebird", "/bin/false", "", ["firebird"], [], []),
                (110, "dhcp", "DHCP", "/dev/null", "/bin/false", "", ["dhcp"], [], []),
                (111, "ldap", "OpenLDAP", "/dev/null", "/bin/false", "", ["ldap"], [], []),
                (112, "clamav", "Clamav", "/dev/null", "/bin/false", "", ["clamav"], [], []),
                (113, "ntlmaps", "NTLMaps", "/dev/null", "/bin/false", "", ["ntlmaps"], [], []),
                (120, "avahi", "Avahi mDNS/DNS-SD Stack", "/run/avahi-daemon", "/sbin/nologin", "", ["avahi"], [], []),
                (121, "avahi-autoipd", "Avahi IPv4LL Stack", "/var/lib/avahi-autoipd", "/sbin/nologin", "", ["avahi-autoipd"], [], []),
                (123, "ntp", "NTP", "/dev/null", "/bin/false", "", ["ntp"], [], []),
                (124, "gdm", "gdm", "/var/lib/gdm", "/sbin/nologin", "", ["gdm"], [], []),
                (130, "tss", "tss", "/var/lib/tpm", "/bin/false", "", ["tss"], [], []),
                (131, "ejabberd", "Ejabberd", "/var/lib/ejabberd", "/bin/false", "", ["ejabberd"], [], []),
                (132, "tomcat", "Tomcat", "/var/lib/tomcat", "/bin/false", "", ["tomcat"], [], []),
                (133, "ups", "UPS", "/var/lib/nut", "/bin/false", "", ["ups", "dialout", "tty", "pnp"], [], []),
                (134, "partimag", "Partimage", "/var/lib/partimaged", "/bin/false", "", ["partimag"], [], []),
                (135, "radiusd", "Freeradius", "/dev/null", "/bin/false", "", ["radiusd"], [], []),
                (136, "oprofile", "oprofile", "/dev/null", "/bin/false", "", ["oprofile"], [], []),
                (137, "mediatomb", "mediatomb", "/dev/null", "/bin/false", "", ["mediatomb"], [], []),
                (138, "pulse", "PulseAudio System Daemon", "/run/pulse", "/bin/false", "", ["pulse", "pulse-access", "pulse-rt", "audio"], [], []),
                (139, "quasselcore", "Quassel IRC System", "/var/cache/quassel", "/bin/false", "", ["quassel"], [], []),
                (140, "bitlbee", "Bitlbee Gateway", "/var/lib/bitlbee", "/bin/false", "", ["bitlbee"], [], []),
                (141, "spamd", "Spamassassin Daemon", "/var/lib/spamd", "/bin/false", "", [], [], []),
                (145, "vboxadd", "VirtualBox Guest Additions", "/dev/null", "/bin/false", "", [], [], []),
                (146, "gnokii", "Gnokii system user", "/", "/sbin/nologin", "", ["gnokii"], [], []),
                (150, "svn", "Subversion", "/dev/null", "/bin/false", "", ["svn"], [], []),
                (151, "icecast", "Icecast Server", "/dev/null", "/bin/false", "", ["icecast"], [], []),
                (152, "memcached", "Memcached daemon", "/run/memcached", "/bin/false", "", ["memcached"], [], []),
                (153, "rtkit", "RealtimeKit", "/proc", "/sbin/nologin", "", ["rtkit"], [], []),
                (154, "nm-openconnect", "NetworkManager user for OpenConnect", "/", "/sbin/nologin", "", ["nm-openconnect"], [], []),
                (160, "usbmuxd", "usbmuxd daemon", "/", "/sbin/nologin", "", ["usbmuxd"], [], []),
                (161, "openvpn", "OpenVPN", "/etc/openvpn", "/sbin/nologin", "", ["openvpn"], [], []),
                (162, "privoxy", "Privoxy", "/etc/privoxy", "/sbin/nologin", "", ["privoxy"], [], []),
                (163, "qemu", "qemu user", "/", "/sbin/nologin", "", ["qemu", "kvm"], [], []),
                (164, "polipo", "polipo user", "/", "/sbin/nologin", "", ["polipo"], [], []),
                (165, "kdm", "kdm", "/var", "/sbin/nologin", "", ["kdm"], [], []),
                (166, "nginx", "nginx user", "/etc/nginx", "/sbin/nologin", "", ["nginx"], [], []),
                (167, "ntop", "ntop user", "/var/lib/ntop", "/sbin/nologin", "", ["ntop"], [], []),
                (168, "smolt", "smolt user", "/dev/null", "/bin/false", "", [], [], []),
                (169, "svxlink", "Svxlink Daemon", "/", "/sbin/nologin", "", ["daemon", "audio", "dialout"], [], []),
                (170, "dansguardian", "Dansguardian web content filter", "/usr/share/dansguardian", "/sbin/nologin", "", ["dansguardian"], [], []),
                (200, "pnp", "PnP", "/dev/null", "/bin/false", "", ["pnp"], [], []),
                (250, "mpd", "Music Player Daemon", "/var/lib/mpd", "/bin/false", "", ["audio", "pulse", "pulse-access", "pulse-rt"], [], []),
                (252, "vdr", "VDR User", "/var/vdr", "/bin/false", "", ["audio", "video", "cdrom", "dialout"], [], []),
            )

    for uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths in users:
        try:
            user = pwd.getpwnam(nick)
        except KeyError:
            hav("addUser", uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths)
        else:
            if user.pw_uid == uid:
                # setUser(uid, realname, homedir, shell, passwd, groups)
                hav("setUser", uid, realname, homedir, shell, password, groups)
            else:
                setUserId(nick, uid)

    # Migrate users to their new groups if any
    migrateUsers()

    # We should only install empty files if these files don't already exist.
    if not os.path.exists("/var/log/lastlog"):
        os.system("/bin/touch /var/log/lastlog")

    if not os.path.exists("/run/utmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /run/utmp")

    if not os.path.exists("/var/log/wtmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/log/wtmp")

    # Enable shadow groups
    os.system("/usr/sbin/grpconv")
    os.system("/usr/sbin/grpck -r &>/dev/null")

    # Create /root if not exists
    if not os.path.exists("/root/"):
        shutil.copytree("/etc/skel", "/root")
        os.chown("/root", 0, 0)
        os.chmod("/root", 0700)

    # Tell init to reload new inittab
    os.system("/sbin/telinit q")

    # Save user defined DNS
    if not os.access("/etc/resolv.default.conf", os.R_OK):
        os.system("cp /etc/resolv.conf /etc/resolv.default.conf")

    # Apply zemberek hack
    zemberek_hack()

    # Fix permissions of /var/lock folder
    os.chown("/var/lock", 0, 54)
    os.chmod("/var/lock", 0775)
