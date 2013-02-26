#!/bin/bash

CHANNEL="release"
BRANCH="releases/mozilla-$CHANNEL"
RELEASE_TAG="FIREFOX_16_0_RELEASE"
VERSION="16.0"

echo "creating compare-locales"
hg clone http://hg.mozilla.org/build/compare-locales
tar cjf compare-locales-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales