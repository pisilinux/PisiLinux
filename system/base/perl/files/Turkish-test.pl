use Turkish 'uc';
use Turkish 'lc';

use utf8;
binmode STDOUT, ':utf8';

print uc("abğıiüşç");
print "\n";
print lc("ABĞIİÜŞÇ");
print "\n";
