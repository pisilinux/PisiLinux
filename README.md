PisiLinux
===
PiSi GNU/Linux devel 
package repository

![Screenshot](http://www.pisilinux.org/wp-content/uploads/2013/03/slide2.jpg)

Dear Developers,

Sevgili Geliştiriciler,

Please be carefull following issues;

Lütfen aşağıdaki konularda dikkatli olalım;

1. There is no systemd in our project that is why we use "--with-systemdsystemunitdir=no" instead of "--with-systemdsystemunitdir=/lib/systemd/system" when we are configure a package.

1. Bizde systemd olmadığı için paketleri yapılandırırken "--with-systemdsystemunitdir=/lib/systemd/system" yerine "--with-systemdsystemunitdir=no" kullanıyoruz.

2. When we are configure a package if we use "--libexecdir=", we use it as "--libexecdir=/usr/lib"

2. Bir paketi yapılandırırken "--libexecdir=" kullanılacaksa "--libexecdir=/usr/lib" böyle olacak.
 
-----------------------------------------------------------------------------------------------------------------------------

[![Throughput Graph](https://graphs.waffle.io/pisilinux/PisiLinux/throughput.svg)](https://waffle.io/pisilinux/PisiLinux/metrics)

