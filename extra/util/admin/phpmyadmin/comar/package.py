#!/usr/bin/python
import random
import string

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # Provide different blowfish cookie key for each computer
    generated_key = ''.join(random.sample(string.letters + string.digits, 32))
    config_path   = '/usr/share/phpmyadmin/config.inc.php'
    new_config    = open(config_path).read().replace('BLOWFISHSECRET', generated_key)
    open(config_path, 'w').write(new_config)

def preRemove():
    pass
