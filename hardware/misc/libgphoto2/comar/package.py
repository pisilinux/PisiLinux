import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    stale_files = ["/usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2-device.fdi",
                   "/etc/udev/rules.d/60-libgphoto2.rules"]

    for f in stale_files:
        if os.path.exists(f):
            os.unlink(f)
