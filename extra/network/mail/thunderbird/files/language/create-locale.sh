#!/bin/bash

CHANNEL="release"
BRANCH="releases/comm-$CHANNEL"
RELEASE_TAG="THUNDERBIRD_15_0_1_RELEASE"
VERSION="15.0.1"

# These are Pardus supported languages. This list may changed by time to time
LOCALES="ca da de es-AR es-ES fr hu it nl pl pt-BR ru"

test ! -d l10n && mkdir l10n
for locale in $LOCALES
do
    hg clone http://hg.mozilla.org/releases/l10n/mozilla-$CHANNEL/$locale l10n/$locale
    [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
done

tar cjf thunderbird-l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=browser --exclude=calendar --exclude=suite l10n
