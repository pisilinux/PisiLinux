PisiLinux
===
PiSi GNU/Linux devel 
package repository

![Screenshot](http://www.pisilinux.org/wp-content/uploads/2013/03/slide2.jpg)

Dear Developers,
Please be carefull following issues;

1. There is no systemd in our project that is why we use "--with-systemdsystemunitdir=no" instead of "--with-systemdsystemunitdir=/lib/systemd/system" when we are configure a package.
2. When we are configure a package we use "--libexecdir=/usr/lib" instead of "--libexecdir=...."
