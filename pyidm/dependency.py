#!/usr/bin/env python
"""
    PyIDM

    multi-connections internet download manager, based on "pyCuRL/curl", "youtube_dl", and "PySimpleGUI"

    :copyright: (c) 2019-2020 by Mahmoud Elshahat.
    :license: GNU LGPLv3, see LICENSE for more details.
"""

# The purpose of this module is checking and auto installing dependencies
import sys
import subprocess
import importlib.util


def install_missing_pkgs():
    ext_pkgs = ['PySimpleGUI', 'pyperclip', 'plyer', 'certifi', 'youtube_dl', 'pycurl', 'PIL']

    # list of dependency
    missing_pkgs = [pkg for pkg in ext_pkgs if importlib.util.find_spec(pkg) is None]

    if missing_pkgs:
        print('required pkgs: ', ext_pkgs)
        print('missing pkgs: ', missing_pkgs)

        for pkg in missing_pkgs:
            # because 'pillow' is installed under different name 'PIL' will use pillow with pip github issue #60
            if pkg == 'PIL':
                pkg = 'pillow'

            cmd = [sys.executable, "-m", "pip", "install", '--user', '--upgrade', pkg]
            print('running command:', ' '.join(cmd))
            subprocess.run(cmd, shell=False)




