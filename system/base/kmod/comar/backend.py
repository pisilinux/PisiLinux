import os
import subprocess

from pardus.fileutils import FileLock

# Config

DIRECTORY_BLACKLIST = "/etc/modprobe.d"
MODULES_DIR = "/lib/modules"
MODULES_CONF = "/etc/modprobe.conf"
MODULES_CONF_DIR = "/etc/modules.d"
MODULES_AUTOLOAD = "/etc/modules.autoload.d/kernel-%s"
MODULES_BLACKLIST = "/etc/modprobe.d/blacklist-compat"
MODULES_COMAR_BLACKLIST = "/etc/modprobe.d/blacklist-comar"

TIMEOUT = 5.0

# l10n

FAIL_TIMEOUT = _({
    "en": "Request timed out. Try again later.",
    "tr": "Talep zaman aşımına uğradı. Daha sonra tekrar deneyin.",
})

FAIL_VERSION = _({
    "en": "Invalid kernel version.",
    "tr": "Geçersiz çekirdek sürümü.",
})

FAIL_PROBE = _({
    "en": "Unable to load module %s: %s",
    "tr": "%s modülü yüklenemedi: %s",
})

FAIL_RMMOD = _({
    "en": "Unable to unload module %s: %s",
    "tr": "%s modülü kaldırılamadı: %s",
})

FAIL_UPDATE = _({
    "en": "Unable to update modprobe.conf: %s",
    "tr": "modprobe.conf güncellenemedi: %s",
})

# Utils

def majorVersion(kernel_version):
    """Parses kernel version and returns major revision."""
    version = kernel_version.split(".")
    if len(version) < 2:
        fail(FAIL_VERSION)
    return ".".join(version[0:2])

class Lock:
    def __init__(self, _file, shared=False):
        lockfile = os.path.join(os.path.dirname(_file), ".%s" % os.path.basename(_file))
        try:
            self.lock = FileLock(_file)
            self.lock.lock(timeout=TIMEOUT, shared=shared)
        except IOError:
            fail(FAIL_TIMEOUT)

    def release(self):
        self.lock.unlock()

def listConfig(_file, prefix=None):
    """Parses given module configuration file and returns modules as a list."""
    lock = Lock(_file, shared=True)
    lines = []
    for line in file(_file):
        line = line.strip()
        if line and not line.startswith("#"):
            lines.append(line)
    lock.release()
    lines = [x.split("#")[0].strip() for x in lines]
    if prefix:
        lines = [x.replace(prefix, "") for x in lines if x.startswith(prefix)]
    return lines

def editConfig(_file, add=[], remove=[], prefix=None):
    """Edits given module list file."""
    lock = Lock(_file, shared=False)
    newlines = []
    if os.path.exists(_file):
        for line in file(_file):
            module = line.strip()
            if prefix and prefix in module:
                module = module.split(prefix)[1]
            if module in remove:
                continue
            if module in add:
                newlines.append("Added through COMAR")
                newlines.append(module)
                add.remove(module)
            else:
                newlines.append(module)
    newlines.extend(add)
    if prefix:
        newlines = ["#Added through COMAR\n%s %s\n" % (prefix, x) for x in newlines if not x.startswith("#")]
    file(_file, "w").write("\n".join(newlines))
    lock.release()

# Boot.Modules methods

def listAvailable():
    """Returns a list of available modules on the system."""
    modules = []
    kernel_version = os.uname()[2]
    path = os.path.join(MODULES_DIR, kernel_version)
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for _file in files:
                if _file.endswith(".ko"):
                    modname = _file[:-3]
                    modules.append(modname)
    return modules

def listLoaded():
    """Returns loaded modules and their options."""
    # Get loaded modules
    modules = {}
    for module in file("/proc/modules"):
        modname = module.split()[0]
        modules[modname] = ""
    # Get options from modprobe.conf
    lock = Lock(MODULES_CONF, shared=True)
    for line in file(MODULES_CONF):
        line = line.strip()
        if line.startswith("options"):
            try:
                command, modname, arguments = line.split(" ", 2)
            except ValueError:
                continue
            if modname in modules:
                modules[modname] = arguments
    lock.release()
    # Build (module: options) list
    list_modules = {}
    for module, options in modules.iteritems():
        list_modules[module] = options
    return list_modules

def setOptions(module, options=""):
    """Sets module options."""
    # Lock modprobe.conf
    lock = Lock(MODULES_CONF, shared=False)
    module_found = False
    # Search for module's config file
    for _file in os.listdir(MODULES_CONF_DIR):
        _file = os.path.join(MODULES_CONF_DIR, _file)
        newlines = []
        for line in file(_file):
            line = line.strip()
            if line.startswith("options %s " % module):
                if options:
                    newlines.append("options %s %s" % (module, options))
                module_found = True
            else:
                newlines.append(line)
        # Update config file
        if module_found:
            file(_file, "w").write("\n".join(newlines))
            break
    # Append module config to "/etc/modules.d/other"
    if not module_found:
        config_file = os.path.join(MODULES_CONF_DIR, "other")
        file(config_file, "a").write("options %s %s" % (module, options))
    # Release lock on modprobe.conf
    lock.release()
    # Update modprobe.conf
    updateModules()

def load(module, options=""):
    """Loads given module with options."""
    cmd = ["/sbin/modprobe", module]
    if options:
        cmd.extend(options.split())
    pipe = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    if pipe.wait() != 0:
        fail(FAIL_PROBE % (module, pipe.stderr.read()))

def unload(module):
    """Unloads given module name."""
    cmd = ["/sbin/rmmod", module]
    pipe = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    if pipe.wait() != 0:
        fail(FAIL_RMMOD % (module, pipe.stderr.read()))

def listAutoload(kernel_version):
    """Lists specified kernel's autoload list."""
    major_release = majorVersion(kernel_version)
    modules_autoload = MODULES_AUTOLOAD % major_release
    modules = []
    if os.path.exists(modules_autoload):
        modules = listConfig(modules_autoload)
    else:
        fail(FAIL_VERSION)
    return modules

def addAutoload(module, kernel_version):
    """Adds module to specified kernel's autoload list."""
    major_release = majorVersion(kernel_version)
    modules_autoload = MODULES_AUTOLOAD % major_release
    editConfig(modules_autoload, add=[module])

def removeAutoload(module, kernel_version):
    """Removes module from specified kernel's autoload list."""
    major_release = majorVersion(kernel_version)
    modules_autoload = MODULES_AUTOLOAD % major_release
    if os.path.exists(modules_autoload):
        editConfig(modules_autoload, remove=[module])
    else:
        fail(FAIL_VERSION)

def listBlacklist():
    """Lists blacklisted modules."""
    modules = []
    if os.path.exists(DIRECTORY_BLACKLIST):
        for f in os.listdir(DIRECTORY_BLACKLIST):
            modules.extend(listConfig(os.path.join(DIRECTORY_BLACKLIST, f), "blacklist "))

    # Make the list unique as there may be some .newconfig in the directory
    return list(set(modules))

def addBlacklist(module):
    """Adds a module to blacklist."""
    editConfig(MODULES_BLACKLIST, add=[module], prefix="blacklist ")

def removeBlacklist(module):
    """Removes module from blacklist."""
    editConfig(MODULES_BLACKLIST, remove=[module], prefix="blacklist ")

def updateModules(kernel_version=None):
    """Updates modprobe.conf"""
    # Lock modprobe.conf
    lock = Lock(MODULES_CONF, shared=False)
    # Run update-modules
    pipe = subprocess.Popen(["/sbin/update-modules"], stderr=subprocess.PIPE)
    reply = pipe.wait()
    # Release lock on modprobe.conf
    lock.release()
    # Return error message on failure
    if reply != 0:
        fail(FAIL_UPDATE % pipe.stderr.read())
    # Run depmod if necessary
    if kernel_version:
        subprocess.call(["/sbin/depmod", "-a", kernel_version])
