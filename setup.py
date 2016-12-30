# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import sys

if 'bdist_wheel' in sys.argv:
    raise RuntimeError("This setup.py does not support wheels")

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wificontrol',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.5.2',

    description='A tool that handles configurations for a network connection via wpa_supplicant',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/MytechIA/wifi_control',

    # Author details
    author='Victor Sonora Pombo',
    author_email='victor.pombo@mytechia.com',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',

        # Operating System
        'Operating System :: POSIX :: Linux',

        # Scope or "topic" of this project
        'Topic :: System :: Networking :: Monitoring'
    ],

    keywords='wifi linux network networking wpa_supplicant',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'wificonfig_conf': ['conf/*']
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    data_files=[('/etc/dbus-1/system.d', ['conf/com.mytechia.wificonfig.conf']),
                ('/lib/systemd/system/', ['conf/wificonfig.service']),
                ('/usr/share/dbus-1/system-services', ['conf/com.mytechia.wificonfig.service']),
                ('/usr/bin', ['conf/wificonfig.sh'])],

    # Unit tests
    test_suite='nose2.collector.collector',

)