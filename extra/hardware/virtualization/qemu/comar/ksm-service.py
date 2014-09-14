from comar.service import *
import os

serviceType = "local"
serviceDefault = "conditional"
serviceDesc = _({"en": "Kernel Samepage Merging",
                 "tr": "Kernel Aynısayfa Birleştirici"})
serviceConf = "ksm"

SYSFS_KSM_RUN = "/sys/kernel/mm/ksm/run"
SYSFS_KSM_MAX_KERNEL_PAGES = "/sys/kernel/mm/ksm/max_kernel_pages"

# unless KSM_MAX_KERNEL_PAGES is set, let ksm munch up to half of total memory.
def default_max_kernel_pages():
    max_kernel_pages = config.get("KSM_MAX_KERNEL_PAGES", "")
    if max_kernel_pages != "":
        return max_kernel_pages

    total = 0
    with open("/proc/meminfo", "r") as _meminfo:
        for line in _meminfo.readlines():
            if "MemTotal" in line:
                total = int(line.split()[-2])
                break

    pagesize = int(os.sysconf("SC_PAGESIZE"))
    return (total * 1024 / pagesize / 2)

@synchronized
def start():
    max_kernel_pages = str(default_max_kernel_pages())
    if os.path.exists(SYSFS_KSM_MAX_KERNEL_PAGES):
        open(SYSFS_KSM_MAX_KERNEL_PAGES, "w").write(max_kernel_pages)

    open(SYSFS_KSM_RUN, "w").write("1")

@synchronized
def stop():
    if os.path.exists(SYSFS_KSM_RUN):
        open(SYSFS_KSM_RUN, "w").write("0")

def ready():
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists(SYSFS_KSM_RUN)):
        start()

def status():
    ret = False
    try:
        ret = (open(SYSFS_KSM_RUN, "r").read().strip() == "1")
    except IOError:
        pass

    return ret

