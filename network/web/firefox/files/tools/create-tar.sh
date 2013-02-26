#!/bin/bash

CHANNEL="release"
BRANCH="releases/mozilla-$CHANNEL"
RELEASE_TAG="FIREFOX_13_0_RELEASE"
VERSION="13.0"

# mozilla
echo "cloning $BRANCH..."
hg clone http://hg.mozilla.org/$BRANCH mozilla
pushd mozilla
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
# get repo and source stamp
echo -n "REV=" > ../source-stamp.txt
hg -R . parent --template="{node|short}\n" >> ../source-stamp.txt
echo -n "REPO=" >> ../source-stamp.txt
hg showconfig paths.default 2>/dev/null | head -n1 | sed -e "s/^ssh:/http:/" >> ../source-stamp.txt
popd
echo "creating archive..."
tar cjf firefox-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

# l10n
echo "fetching locales..."
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' mozilla/browser/locales/shipped-locales); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      echo "fetching $locale ..."
      hg clone http://hg.mozilla.org/releases/l10n/mozilla-$CHANNEL/$locale l10n/$locale
      [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
echo "creating l10n archive..."
tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

# compare-locales
echo "creating compare-locales"
hg clone http://hg.mozilla.org/build/compare-locales
tar cjf compare-locales.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

