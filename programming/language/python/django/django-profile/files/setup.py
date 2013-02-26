from setuptools import setup, find_packages

setup(name='userprofile',
        version='0.6',
        description='Django pluggable user profile zone',
        author='David Rubert',
        packages=find_packages(),
        classifiers=['Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'],
    include_package_data=True,
    install_requires=['setuptools'],
    package_data = {
        'userprofile' : [ 'templates/userprofile/*.html', 'templates/userprofile/account/*.html', 'templates/userprofile/account/includes/*.html', 'templates/userprofile/avatar/*.html', 'templates/userprofile/email/*.txt', 'templates/userprofile/profile/*.html', 'locale/*/*/*', ]
    },
)
