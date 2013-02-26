# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#

import os
import glob
import fcntl
import random
import shutil
import hashlib

from string import ascii_letters, digits
from pardus.fileutils import FileLock

try:
    import polkit
except ImportError:
    pass


# faces

FACES = [
    "/usr/share/kde4/apps/kdm/pics/users",
]

# messages

invalid_username_msg = {
    "en": "User name is invalid.",
    "tr": "Kullanıcı adı geçersiz.",
    "fr": "Nom d'utilisateur invalide.",
    "es": "Nombre de usuario no es válido.",
    "de": "Benutzername nicht erlaubt.",
    "nl": "Gebruikernaam is ongeldig.",
}

invalid_realname_msg = {
    "en": "Real name is invalid.",
    "tr": "Gerçek isim geçersiz.",
    "fr": "Nom réel invalide.",
    "es": "Nombre real no es válido.",
    "de": "Dieser vollständige Name ist nicht erlaubt.",
    "nl": "Echte naam is ongeldig.",
}

short_password_msg = {
    "en": "Password is too short.",
    "tr": "Parola çok kısa.",
    "fr": "Mot de passe trop court.",
    "es": "Contraseña es demadiado corta.",
    "de": "Passwort ist zu kurz.",
    "nl": "Wachtwoord is te kort.",
}

name_password_msg = {
    "en": "Dont use your name as a password.",
    "tr": "Adınızı parola olarak kullanmayın.",
    "fr": "N'utilisez pas votre nom comme mot de passe.",
    "es": "No use su nombre como contraseña.",
    "de": "Benutzen Sie nicht Ihren Namen als Passwort.",
    "nl": "Uw naam niet als wachtwoord gebruiken.",
}

invalid_group_msg = {
    "en": "Invalid group name:",
    "tr": "Geçersiz grup adı:",
    "fr": "Nom de groupe invalide:",
    "es": "Nombre de grupo inválido:",
    "de": "Gruppenname nicht erlaubt:",
    "nl": "Ongeldige groepnaam:",
}

invalid_userid_msg = {
    "en": "Invalid user ID.",
    "tr": "Geçersiz kullanıcı numarası.",
    "fr": "Identifiant utilisateur invalide.",
    "es": "ID de usuario no válido.",
    "de": "User-ID nicht erlaubt.",
    "nl": "Gebruiker-id is ongeldig.",
}

used_userid_msg = {
    "en": "This user ID is already used.",
    "tr": "Bu kullanıcı numarası zaten kullanılmakta.",
    "fr": "Cet identifiant utilisateur est déjà utilisé.",
    "es": "Este ID de usuario ya está en uso.",
    "de": "Dieser user-ID is schon vergeben.",
    "nl": "Deze gebruiker-id is reeds in gebruik.",
}

used_username_msg = {
    "en": "This user name is already used.",
    "tr": "Bu kullanıcı adı zaten kullanılmakta.",
    "fr": "Ce nom d'utilisateur est déjà utilisé.",
    "es": "Este nombre de usuario ya está en uso.",
    "de": "Dieser Benutzername is schon vergeben.",
    "nl": "Deze gebruikernaam is reeds in gebruik.",
}

no_group_msg = {
    "en": "No such group exists.",
    "tr": "Böyle bir grup yok.",
    "fr": "Il n'existe aucun groupe de ce nom-là.",
    "es": "No existe el grupo.",
    "de": "Diese Gruppe gibt es nicht.",
    "nl": "Deze groep bestaat niet.",
}

no_user_msg = {
    "en": "No user with given ID.",
    "tr": "Verilen numaralı bir kullanıcı yok.",
    "fr": "Il n'existe aucun utilisateur avec et identifiant.",
    "es": "No existe usuario con éste ID.",
    "de": "Es gibt keien Benutzer mit dem angegebenen ID.",
    "nl": "Gebruiker met opgegeven ID bestaat niet.",
}

delete_root_msg = {
    "en": "You cant delete root user.",
    "tr": "Kök kullanıcıyı silemezsiniz.",
    "fr": "Vous ne pouvez pas supprimer l'administrateur.",
    "es": "No se puede eliminar al usuario root.",
    "de": "Benutzer ROOT darf nicht gelöscht werden.",
    "nl": "Systeembeheerder (root) kan niet verwijderd worden.",
}

invalid_groupid_msg = {
    "en": "Invalid group ID.",
    "tr": "Geçersiz grup numarası.",
    "fr": "Identifiant de groupe invalide.",
    "es": "ID del grupo inválido.",
    "de": "Gruppen-ID nicht zulässig.",
    "nl": "Groep-ID is ongeldig.",
}

used_groupid_msg = {
    "en": "This group ID is already used.",
    "tr": "Bu grup numarası zaten kullanılmakta.",
    "fr": "Cet identifiant de groupe est déjà utilisé.",
    "es": "Este ID de grupo ya está en uso.",
    "de": "Dieser Gruppen-ID is schon vergeben.",
    "nl": "Deze groep-ID is reeds in gebruik.",
}

used_groupname_msg = {
    "en": "This group name is already used.",
    "tr": "Bu grup adı zaten kullanılmakta.",
    "fr": "Ce nom de groupe est déjà utilisé.",
    "es": "Este nombre de grupo ya está en uso.",
    "de": "Dieser Gruppennam is schon vergeben.",
    "nl": "Deze groepnaam is reeds in gebruik.",
}

# parameters
uid_minimum = 1000
uid_maximum = 65000

#

def setFace(uid, homedir):
    files = []
    for directory in FACES:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if filename.endswith(".png"):
                    files.append(os.path.join(directory, filename))
    if len(files):
        icon = os.path.join(homedir, ".face.icon")
        shutil.copy(random.choice(files), icon)
        os.chmod(icon, 0644)
        os.chown(icon, uid, 100)

def checkName(name):
    first_valid = ascii_letters
    valid = ascii_letters + "_-" + digits
    if len(name) == 0 or len(filter(lambda x: not x in valid, name)) != 0 or not name[0] in first_valid:
        fail(_(invalid_username_msg))

def checkRealName(realname):
    if len(filter(lambda x: x == "\n" or x == ":", realname)) != 0:
        fail(_(invalid_realname_msg))

def checkPassword(password, badlist):
    if len(password) < 1:
        fail(_(short_password_msg))
    if password in badlist:
        fail(_(name_password_msg))

def checkGroupName(name):
    valid = ascii_letters + "_-"
    if name == "" or len(filter(lambda x: not x in valid, name)) != 0:
        fail(_(invalid_group_msg) + " " + name)

#

class User:
    def __init__(self):
        self.password = None

    def __str__(self):
        return "%s (%d, %d)\n  %s\n  %s\n  %s\n  %s" % (
            self.name, self.uid, self.gid,
            self.realname, self.homedir, self.shell,
            self.password
        )


class Group:
    def __str__(self):
        s = "%s (%d)" % (self.name, self.gid)
        for name in self.members:
            s += "\n %s" % name
        return s


class Database:
    passwd_path = "/etc/passwd"
    shadow_path = "/etc/shadow"
    group_path = "/etc/group"
    lock_path = "/etc/.pwd.lock"

    def __init__(self, for_read=False):
        self.lock = FileLock(self.lock_path)
        self.lock.lock(shared=for_read)

        self.users = {}
        self.users_by_name = {}
        self.groups = {}
        self.groups_by_name = {}

        for line in file(self.passwd_path):
            if line != "" and line != "\n":
                parts = line.rstrip("\n").split(":")
                user = User()
                user.name = parts[0]
                user.uid = int(parts[2])
                user.gid = int(parts[3])
                user.realname = parts[4]
                user.homedir = parts[5]
                user.shell = parts[6]
                self.users[user.uid] = user
                self.users_by_name[user.name] = user

        for line in file(self.shadow_path):
            if line != "" and line != "\n":
                parts = line.rstrip("\n").split(":")
                if self.users_by_name.has_key(parts[0]):
                    user = self.users_by_name[parts[0]]
                    user.password = parts[1]
                    user.pwrest = parts[2:]

        for line in file(self.group_path):
            if line != "" and line != "\n":
                parts = line.rstrip("\n").split(":")
                group = Group()
                group.name = parts[0]
                group.gid = int(parts[2])
                group.members = parts[3].split(",")
                if "" in group.members:
                    group.members.remove("")
                self.groups[group.gid] = group
                self.groups_by_name[group.name] = group

    def sync(self):
        lines = []
        keys = self.users.keys()
        keys.sort()
        for uid in keys:
            user = self.users[uid]
            lines.append("%s:x:%d:%d:%s:%s:%s\n" % (
                user.name, uid, user.gid,
                user.realname, user.homedir, user.shell
            ))
        f = file(self.passwd_path, "w")
        f.writelines(lines)
        f.close()

        lines = []
        keys = self.users.keys()
        keys.sort()
        for uid in keys:
            user = self.users[uid]
            if user.password:
                lines.append("%s:%s:%s\n" % (
                    user.name,
                    user.password,
                    ":".join(user.pwrest)
                ))
            else:
                lines.append("%s::13094:0:99999:7:::\n" % user.name)
        f = file(self.shadow_path, "w")
        f.writelines(lines)
        f.close()

        lines = []
        keys = self.groups.keys()
        keys.sort()
        for gid in keys:
            group = self.groups[gid]
            lines.append("%s:x:%s:%s\n" % (group.name, gid, ",".join(group.members)))
        f = file(self.group_path, "w")
        f.writelines(lines)
        f.close()

    def set_groups(self, name, grouplist):
        for gid in self.groups.keys():
            g = self.groups[gid]
            if name in g.members:
                if not g.name in grouplist:
                    g.members.remove(name)
            else:
                if g.name in grouplist:
                    g.members.append(name)

    def next_uid(self):
        for i in range(uid_minimum, uid_maximum):
            if not self.users.has_key(i):
                return i

    def next_gid(self):
        for i in range(uid_minimum, uid_maximum):
            if not self.groups.has_key(i):
                return i


def setup_home(uid, gid, path):
    if not os.path.exists(path):
        # Copy skeleton home dir
        os.system('/bin/cp -r %s "%s"' % ('/etc/skel', path))
        # Set a random face icon
        faces = glob.glob("/usr/share/*/apps/kdm/pics/users/*.png")
        if len(faces) > 0:
            facepath = os.path.join(path, '.face.icon')
            os.system('/bin/cp --remove-destination "%s" "%s"' % (random.choice(faces), facepath))
            os.chmod(facepath, 0644)
        # Set ownerships
        os.system('/bin/chown -R %d:%d "%s"' % (uid, gid, path))

    # Make sure at least top of the home dir's permissions are correct
    os.system('/bin/chown %d:%d "%s"' % (uid, gid, path))
    os.chmod(path, 0711)


# methods

def userList():
    def format(dict, uid):
        item = dict[uid]
        return (item.uid, item.name, item.realname)
    db = Database(for_read=True)
    return map(lambda x: format(db.users, x), db.users)

def userInfo(uid):
    uid = int(uid)
    db = Database(for_read=True)
    if db.users.has_key(uid):
        u = db.users[uid]
        groups = []
        for item in db.groups.keys():
            if u.name in db.groups[item].members:
                groups.append(db.groups[item].name)
        grp = db.groups.get(u.gid, None)
        if grp:
            if grp.name in groups:
                groups.remove(grp.name)
            groups.insert(0, grp.name)
        ret = (
            u.name,
            u.realname,
            u.gid,
            u.homedir,
            u.shell,
            groups,
        )
        return ret
    else:
        fail(_(no_user_msg))

def addUser(uid, name, realname, homedir, shell, password, groups, grants, blocks):
    if not realname:
        realname = ""
    if not homedir:
        homedir = "/home/" + name
    if not shell:
        shell = "/bin/bash"
    if not groups:
        groups = ["nogroup"]
    for item in groups:
        checkGroupName(item)
    checkName(name)
    checkRealName(realname)
    if password:
        checkPassword(password, (name, realname))

    db = Database()

    if uid == -1:
        uid = db.next_uid()
    else:
        try:
            uid = int(uid)
            if uid < 0 or uid > 65536:
                raise
        except:
            fail(_(invalid_userid_msg))
        if db.users.has_key(uid):
            fail(_(used_userid_msg))

    if db.users_by_name.has_key(name):
        fail(_(used_username_msg))

    # First group in the list is the user's main group
    g = db.groups_by_name.get(groups[0], None)
    if not g:
        fail(_(no_group_msg))
    gid = g.gid

    u = User()
    u.uid = uid
    u.gid = gid
    u.name = name
    u.realname = realname
    u.homedir = homedir
    u.shell = shell
    if password:
        u.password = shadowCrypt(password)
    else:
        u.password = "*"
    u.pwrest = [ "13094", "0", "99999", "7", "", "", "" ]
    db.users[uid] = u
    db.set_groups(name, groups)
    # No need to setup a real home dir for daemons
    if uid >= 1000 or homedir.startswith("/home/"):
        setup_home(uid, gid, homedir)
        setFace(uid, homedir)
    db.sync()

    for grant in grants:
        if grant != "":
            grantAuthorization(uid, grant)
    for block in blocks:
        if block != "":
            blockAuthorization(uid, block)

    return uid

def setUser(uid, realname, homedir, shell, password, groups):
    uid = int(uid)

    db = Database()
    u = db.users.get(uid, None)
    if u:
        if realname:
            checkRealName(realname)
            u.realname = realname
        if homedir:
            u.homedir = homedir
        if shell:
            u.shell = shell
        if password:
            checkPassword(password, (u.name, u.realname, realname))
            u.password = shadowCrypt(password)
        if groups:
            # FIXME: check main group
            for item in groups:
                checkGroupName(item)
            db.set_groups(u.name, groups)
        db.sync()
    else:
        fail(_(no_user_msg))

def deleteUser(uid, deletefiles):
    uid = int(uid)

    if uid == 0:
        fail(_(delete_root_msg))

    db = Database()
    u = db.users.get(uid, None)
    if u:
        #delete authorizations of user
        try:
            polkit.auth_revoke_all(uid)
        except:
            pass

        home = u.homedir[:]
        db.set_groups(u.name, [])
        del db.users[uid]
        db.sync()
        if deletefiles:
            os.system('/bin/rm -rf "%s"' % home)


def groupList():
    def format(dict, gid):
        item = dict[gid]
        return (item.gid, item.name)
    db = Database(for_read=True)
    return map(lambda x: format(db.groups, x), db.groups)

def addGroup(gid, name):
    checkGroupName(name)

    db = Database()
    if gid == -1:
        gid = db.next_gid()
    else:
        try:
            gid = int(gid)
            if gid < 0 or gid > 65536:
                raise
        except:
            fail(_(invalid_groupid_msg))
        if db.groups.has_key(gid):
            fail(_(used_groupid_msg))

    if db.groups_by_name.has_key(name):
        fail(_(used_groupname_msg))

    g = Group()
    g.gid = gid
    g.name = name
    g.members = []
    db.groups[gid] = g
    db.sync()

    return gid

def deleteGroup(gid):
    gid = int(gid)

    db = Database()
    if db.groups.has_key(gid):
        del db.groups[gid]
        db.sync()


#
# Crypt function for shadow file
#

def shadowCrypt(password):
    des_salt = list('./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    salt, magic = str(random.random())[-8:], '$1$'

    ctx = hashlib.md5(password)
    ctx.update(magic)
    ctx.update(salt)

    ctx1 = hashlib.md5(password)
    ctx1.update(salt)
    ctx1.update(password)

    final = ctx1.digest()

    for i in range(len(password), 0 , -16):
        if i > 16:
            ctx.update(final)
        else:
            ctx.update(final[:i])

    i = len(password)

    while i:
        if i & 1:
            ctx.update('\0')
        else:
            ctx.update(password[:1])
        i = i >> 1
    final = ctx.digest()

    for i in range(1000):
        ctx1 = hashlib.md5()
        if i & 1:
            ctx1.update(password)
        else:
            ctx1.update(final)
        if i % 3: ctx1.update(salt)
        if i % 7: ctx1.update(password)
        if i & 1:
            ctx1.update(final)
        else:
            ctx1.update(password)
        final = ctx1.digest()

    def _to64(v, n):
        r = ''
        while (n-1 >= 0):
            r = r + des_salt[v & 0x3F]
            v = v >> 6
            n = n - 1
        return r

    rv = magic + salt + '$'
    final = map(ord, final)
    l = (final[0] << 16) + (final[6] << 8) + final[12]
    rv = rv + _to64(l, 4)
    l = (final[1] << 16) + (final[7] << 8) + final[13]
    rv = rv + _to64(l, 4)
    l = (final[2] << 16) + (final[8] << 8) + final[14]
    rv = rv + _to64(l, 4)
    l = (final[3] << 16) + (final[9] << 8) + final[15]
    rv = rv + _to64(l, 4)
    l = (final[4] << 16) + (final[10] << 8) + final[5]
    rv = rv + _to64(l, 4)
    l = final[11]
    rv = rv + _to64(l, 2)

    return rv

#
# List authorizations by UID
#

def listUserAuthorizations(uid):
    actions = polkit.auth_list_uid(int(uid))
    auths = []
    for action in actions:
        action_info = polkit.action_info(action['action_id'])
        auths.append((action['action_id'], action['scope'], action_info['description'], action_info['policy_active'], action['negative']))
    return auths

#
# Grant authorization to user
#

def grantAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_add(action_id, polkit.SCOPE_ALWAYS, uid)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_add(action, polkit.SCOPE_ALWAYS, uid)
        except:
            return False
    return True

#
# Revoke authorization of user
#

def revokeAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
        except:
            return False
    return True

#
# Block authorization of user
#

def blockAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_block(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_block(uid, action)
        except:
            return False
    return True
