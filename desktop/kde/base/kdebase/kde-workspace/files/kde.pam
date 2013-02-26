#%PAM-1.0

auth       include      system-auth
auth       required     pam_nologin.so

account    include      system-auth

password   include      system-auth

session    include      system-auth

session    optional     pam_console.so
session    optional     pam_polkit_console.so
