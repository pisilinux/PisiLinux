#!/bin/sh
export CHROME_WRAPPER=/usr/lib/chromium-browser/chromium-browser
export CHROME_DESKTOP=chromium-browser.desktop
exec /usr/lib/chromium-browser/chromium-browser "$@"
