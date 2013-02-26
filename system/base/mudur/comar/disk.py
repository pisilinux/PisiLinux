#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import sys
import subprocess

FSTAB = '/etc/fstab'

"""
Quick list is used for improving efficiency of the script.
Stores device names and uuids pairs for partitions so prevents multiple
communication with subprocesses.
"""
quickList = {}

FAIL_FSTAB = {
    "en": "Unable to read '%s'.",
    "tr": "'%s' okunamadı.",
    "fr": "Impossible de lire '%s' .",
    "es": "No posible leer '%s'.",
    "de": "'%s' konnte nicht gelesen werden.",
    "nl": "Kan '%s' niet lezen.",
}

FAIL_PATH = {
    "en": "'%s' is not a valid mount point.",
    "tr": "'%s' geçerli bir bağlama noktası değil.",
    "fr": "'%s' n'est pas un point de montage valide.",
    "es": "'%s' no es un punto de montaje válido.",
    "de": "'%s' ist kein gültiger Mount-Punkt.",
    "nl": "'%s' is geen geldig aankoppelpunt.",
}

FAIL_PATH_ALREADY_EXIST = {
    "en": "'%s' is already being used by an entry.",
    "tr": "'%s' zaten bir kayıt tarafından kullanılıyor.",
    "fr": "'%s' est déjà utilisé par une entrée.",
    "es": "Ya '%s' siendo utilizado por una entrada.",
    "de": "'%s' wird bereits durch einen Eintrag verwendet.",
    "nl": "'%s' bruges allerede af en post.",
}

FAIL_ENTRY = {
    "en": "Device '%s' not found in entry list.",
    "tr": "'%s' aygıtı listede bulunamadı.",
    "fr": "Le matériel '%s' n'a pas été trouvé dans la liste.",
    "es": "Dispositivo '%s' no encontrado en lista de entrada.",
    "de": "Gerät '%s' ist nicht in der Liste eingetragen.",
    "nl": "Apparaat '%s' is niet in invoerlijst gevonden.",
}

FAIL_ROOT = {
    "en": "'%s' is mounted to root directory, operation cancelled.",
    "tr": "'%s' diski kök dizine bağlı, işlem iptal edildi.",
    "fr": "'%s' est monté sur le répertoire racine, opération annulée.",
    "es": "'%s' está montado com root, operación cancelada.",
    "de": "'%s' ist als Root gemounted, Vorgang abgebrochen.",
    "nl": "'%s' is in root-map aangekoppeld, bewerking geannuleerd.",
}

FAIL_MOUNTED = {
    "en": "'%s' is mounted to another directory, operation cancelled.",
    "tr": "'%s' başka bir dizine bağlı, işlem iptal edildi.",
    "fr": "'%s' est monté sur un autre répertoire, opération annulée.",
    "es": "'%s' está montado en otro directorio, operación cancelada.",
    "de": "'%s' ist schon auf einem anderen Mount-Punkt gemounted, Vorgang abgebrochen.",
    "nl": "'%s' is in een andere map aangekoppeld, bewerking geannuleerd.",
}

FAIL_OPERATION = {
    "en": "Operation failed:\n\n %s",
    "tr": "İşlem başarısız:\n\n %s",
    "fr": "L'opération a échoué : \n\n %s",
    "es": "Operación fallada:\n\n %s",
    "de": "Vorgang fehlerhaft:\n\n %s",
    "nl": "Mislukte bewerking:\n\n %s",
}

class DMException(Exception):
    pass

def parseFstab(fstab):
    if not os.access(fstab, os.R_OK):
        raise DMException, _(FAIL_FSTAB) % fstab
    entries = []
    for line in open(fstab):
        line = line.strip()
        # Check len(line) for empty lines.
        if line.startswith('#') or len(line) == 0:
            continue
        line = line.replace('\t', ' ').split()
        # Replace UUID value with device name after reading it from fstab
        if line[0].startswith('UUID='):
            line[0] = getPartitionNameByUUID(line[0])
            entries.append(line)
        elif line[0].startswith('LABEL='):
            line[0] = getDeviceByLabel(line[0].replace('LABEL=', ''))
            entries.append(line)
        elif line[0].startswith('/dev/'):
            entries.append(line)
    return entries

def createPath(device, path):
    real_path = path
    if not os.path.exists(path) and os.path.exists(os.path.dirname(path)):
        # Mount point does not exist, but parent directory does.
        path = os.path.dirname(path)
        if not os.path.ismount(path) and not os.path.islink(path) and os.path.isdir(path):
            os.mkdir(real_path, 0755)
            return True
    else:
        if os.path.ismount(path):
            # Path is already mounted, allow user to use that mount point if it's already mounted
            for _device, _path in getMounted():
                if device == _device and _path == path:
                    return True
        else:
            if not os.path.islink(path) and os.path.isdir(path) and os.listdir(path) == []:
                return True
    return False

def getMounted():
    parts = []
    for line in open('/proc/mounts'):
        if line.startswith('/dev/'):
            device, path, other = line.split(" ", 2)
            parts.append((device, path, ))
    return parts

def getFSType(device):
    if device.startswith('UUID='):
        device = getPartitionNameByUUID(device)
    cmd = "/sbin/blkid -s TYPE -o value %s" % device
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    return proc.communicate()[0].strip()

def getUUID(part):
    """
    Finds UUID for the given partition.
    """
    global quickList
    if len(quickList) == 0:
        fillQuickList()
    return quickList[part]

def getPartitionNameByUUID(part):
    """
    Finds name of the partition for the given UUId.
    """
    global quickList
    part = part.replace('UUID=', '')
    if len(quickList) == 0:
        fillQuickList()
    for devName, uuid in quickList.items():
        if uuid == part:
            return devName
    return ''

def fillQuickList():
    """
    Fills the quick list.
    """
    global quickList
    cmd = "/sbin/blkid"
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    for line in proc.stdout:
        line = line.replace(':', '').strip()
        propList = line.split()
        devName = label = uuid = fsType = ''
        devName = propList[0]
        for property in propList:
            if property.startswith('UUID'):
                uuid = property.replace('UUID=', '').replace('"', '')
        quickList[devName] = uuid

def runCommand(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = proc.communicate()[1].strip()
    if len(err):
        fail(_(FAIL_OPERATION) % err)

# Disk.Manager methods

def isMounted(device):
    """
    Searches the given partition in mounted devices. If partition is
    mounted, returns mount point else returns none.
    """
    for _device, _path in getMounted():
        if device == _device:
            return _path
    return ''

def getDevices():
    from pardus.diskutils import EDD
    return EDD().blockDevices()

def getDeviceByLabel(label):
    root = '/dev/disk/by-label'
    path = os.path.join(root, label)
    if os.access(path, os.R_OK):
        return os.path.realpath(os.path.join(root, os.readlink(path)))
    else:
        return ''

def getDeviceParts(device):
    if not os.path.exists(device):
        return []
    parts = []
    for part in glob.glob("%s*" % device):
        if not part == device and not getFSType(part) == "":
            parts.append(part)
    return parts

def getLabel(device):
    """
    Finds label for the given partition.
    """
    cmd = "/sbin/blkid -s LABEL -o value %s" % device
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    return proc.communicate()[0].strip()

def getPath(device):
    """
    Gets partition name and determine a path for that partition.
    """
    # If there is a entry record for this partition in fstab
    # use path in there.
    if device in listEntries():
        path_, fsType_, options_ = getEntry(device)
        return path_
    path = '/media/'
    label = getLabel(device)
    # There may be partitions without a label
    if not label:
        if not os.path.exists(path+'disk'):
            path = path+'disk'
        elif not os.path.ismount(path+'disk'):
            path = path+'disk'
        else:
            for i in range(1, len(getMounted())):
                if not os.path.exists(path+'disk-'+str(i)):
                    path = path+'disk-'+str(i)
                    break
                elif not os.path.ismount(path+'disk-'+str(i)):
                    path = path+'disk-'+str(i)
                    break
    # Labels may be same
    else:
        if not os.path.exists(path+label):
            path = path+label
        elif not os.path.ismount(path+label):
            path = path+label
        else:
            for i in range(1, len(getMounted())):
                if not os.path.exists(path+label+'-'+str(i)):
                    path = path+label+'-'+str(i)
                    break
                elif not os.path.ismount(path+label+'-'+str(i)):
                    path = path+label+'-'+str(i)
                    break
    return path

def mount(device, path):
    if not path:
        path = getPath(device)
        if not createPath(device, path):
            # Can't create new path
            fail(_(FAIL_PATH) % path)
        elif device in [x[0] for x in getMounted()]:
            # Device is mounted
            fail(_(FAIL_MOUNTED) % device)
    runCommand(['/bin/mount', device, path])

def umount(device):
    for dev, path in getMounted():
        if dev == device and path == "/":
            fail(_(FAIL_ROOT) % device)
    runCommand(['/bin/umount', device])

def listEntries():
    try:
        devices = [x[0] for x in parseFstab(FSTAB)]
        return devices
    except DMException:
        return []

def listPaths():
    """
    Return paths of the entries in fstab.
    """
    try:
        paths = [x[1] for x in parseFstab(FSTAB)]
        return paths
    except DMException:
        return []

def isLabelRecord(device):
    for line in open(FSTAB):
        line = line.strip().replace('\t', ' ').split()
        if line:
            if line[0] == 'LABEL=' + getLabel(device):
                return True

def addEntry(device, path, fsType, options):
    path_own = False
    if device in listEntries():
        old_path, old_fsType, old_options = getEntry(device)
        # Do not change root
        if old_path == "/" and not old_path == path:
            fail(_(FAIL_ROOT) % device)
        # Who has that mount point? me?
        if old_path == path:
            path_own = True
    else:
        # If the path value already exist in fstab, cut the operation
        if path in listPaths():
                fail(_(FAIL_PATH_ALREADY_EXIST) % path)
        old_path = None
        if not createPath(device, path):
            # Can't create new path
            fail(_(FAIL_PATH) % path)
        #elif device in [x[0] for x in getMounted()]:
            # Device is mounted
            #fail(_(FAIL_MOUNTED) % device)
    partText = ''
    # Before removing the entry check if it is a label record or uuid record
    # Remove previous one to prevent duplicates
    if old_path:
        if isLabelRecord(device):
            partText = 'LABEL='+getLabel(device)
        else:
            partText = 'UUID='+getUUID(device)
    else:
        partText = 'UUID='+getUUID(device)
    # Add new entry
    _options = []
    for key, value in options.iteritems():
        if value:
            _options.append('%s=%s' % (key, value))
        else:
            _options.append(key)
    if not file(FSTAB).read()[-1] == '\n':
        file(FSTAB, 'a').write('\n')
    _options = ','.join(_options)

    addit = True
    # If the partition is not already mounted the given path and,
    # if the partition is not mounted anywhere, try to create a path
    # and mount there.
    if not path_own:
        if not createPath(device, path):
            addit = False
            # Can't create new path
            fail(_(FAIL_PATH) % path)
        if not device in [x[0] for x in getMounted()]:
            # Mount device
            try:
                mount(device, path)
            except:
                addit = False
                raise
    if addit:
        # try to remove old entry before
        if old_path:
            removeEntry(device, silent=True)
        if _options:
            file(FSTAB, 'a').write('%s %s %s %s 0 0\n' % (partText, path, fsType, _options))
        else:
            file(FSTAB, 'a').write('%s %s %s defaults 0 0\n' % (partText, path, fsType))
        # Notify clients
        notify("Disk.Manager", "changed", ())

def getEntry(device):
    entries = parseFstab(FSTAB)
    for entry in entries:
        if entry[0] == device:
            _path, _fsType, _options, _dump, _pass = entry[1:]
            options = {}
            for part in _options.split(','):
                if "=" in part:
                    key, value = part.split('=', 1)
                    options[key] = value
                else:
                    options[part] = ""
            return _path, _fsType, options
    fail(_(FAIL_ENTRY) % device)

def removeEntry(device, silent=False):
    if isMounted(device) == '/':
        fail(_(FAIL_ROOT) % device)
    if device not in listEntries():
        return
    newlines = []
    for line in open(FSTAB):
        line = line.strip()
        if not len(line) == 0 and not (line.replace('\t', ' ').split()[0] == 'UUID='+getUUID(device) or line.replace('\t', ' ').split()[0] == 'LABEL='+getLabel(device) or line.replace('\t', ' ').split()[0] == device):
            newlines.append(line)
    file(FSTAB, 'w').write('\n'.join(newlines))
    if not file(FSTAB).read()[-1] == '\n':
        file(FSTAB, 'a').write('\n')
    # Notify clients
    if not silent:
        notify("Disk.Manager", "changed", ())


import errno
from time import sleep
from fcntl import ioctl

# Path to sync executable
PATH_SYNC = '/bin/sync'

# Emulate required asm-generic/ioctl.h macros
_IOC_NRBITS    = 8
_IOC_TYPEBITS  = 8
_IOC_SIZEBITS  = 14
_IOC_DIRBITS   = 2

_IOC_NRMASK    = ((1 << _IOC_NRBITS)   - 1)
_IOC_TYPEMASK  = ((1 << _IOC_TYPEBITS) - 1)
_IOC_SIZEMASK  = ((1 << _IOC_SIZEBITS) - 1)
_IOC_DIRMASK   = ((1 << _IOC_DIRBITS)  - 1)

_IOC_NRSHIFT   = 0
_IOC_TYPESHIFT = (_IOC_NRSHIFT   + _IOC_NRBITS)
_IOC_SIZESHIFT = (_IOC_TYPESHIFT + _IOC_TYPEBITS)
_IOC_DIRSHIFT  = (_IOC_SIZESHIFT + _IOC_SIZEBITS)

# Direction bits.
_IOC_NONE      = 0
_IOC_WRITE     = 1
_IOC_READ      = 2

def _IOC(dir,type,nr,size):
    return (((dir)  << _IOC_DIRSHIFT)  | \
            (type   << _IOC_TYPESHIFT) | \
            ((nr)   << _IOC_NRSHIFT)   | \
            ((size) << _IOC_SIZESHIFT))

def _IO(type, nr):
    """Note: type is specified in hex and nr in decimal."""
    return _IOC(_IOC_NONE,(type),(nr),0)

def BLKRRPART():
    """Returns ioctl number for re-reading partition table."""
    # Kernels >2.6.17 have BLKRRPART defined in include/linux/fs.h.
    return _IO(0x12, 95)
# -------------------------------------------

def refreshPartitionTable(device):
    """Re-Read partition table on device."""

    try:
        fd = os.open(device, os.O_RDONLY)
    except EnvironmentError, (error, strerror):
        print 'Could not open device %s. Reason: %s.'%(device, strerror)
        sys.exit(-1)

    # Sync and wait for Sync to complete
    os.system(PATH_SYNC)
    sleep(2)

    # Call required ioctl to re-read partition table
    try:
        ioctl(fd, BLKRRPART())
    except EnvironmentError, (error, message):
        # Attempt ioctl call twice in case an older kernel (1.2.x) is being used
        os.system(PATH_SYNC)
        sleep(2)

        try:
            ioctl(fd, BLKRRPART())
        except EnvironmentError, (error, strerror):
            print 'IOCTL Error: %s for device %s.'%(strerror, device)
            sys.exit(-1)

    print 'Successfully re-read partition table on device %s.'%(device)
    # Sync file buffers
    os.fsync(fd)
    os.close(fd)

    # Final sync
    print "Syncing %s ...  " % (device),
    os.system(PATH_SYNC)
    sleep(4) # for sync()
    print "Done."



