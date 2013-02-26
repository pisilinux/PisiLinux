#!/bin/bash

CHANNEL="release"
BRANCH="releases/mozilla-$CHANNEL"
RELEASE_TAG="FIREFOX_10_0_RELEASE"
VERSION="10.0"

test ! -d mozilla && mkdir mozilla
hg clone http://hg.mozilla.org/$BRANCH mozilla
pushd mozilla
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd

tar cjf firefox-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

