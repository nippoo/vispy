# -*- coding: utf-8 -*-
# Copyright (c) 2015, Vispy Development Team.
# This shim has been imported from Astropy.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Handle loading six package from system or from the bundled copy
"""

import imp
import io

from distutils.version import StrictVersion


_SIX_MIN_VERSION = StrictVersion('1.4.1')


def _find_module(name, path=None):
    """
    Alternative to `imp.find_module` that can also search in subpackages.
    """

    parts = name.split('.')

    for part in parts:
        if path is not None:
            path = [path]

        fh, path, descr = imp.find_module(part, path)

    return fh, path, descr


for mod_name in ['vispy.ext._bundled.six', 'six']:
    try:
        mod_info = _find_module(mod_name)
    except ImportError:
        continue

    mod = imp.load_module(__name__, *mod_info)

    try:
        if StrictVersion(mod.__version__) >= _SIX_MIN_VERSION:
            break
    except (AttributeError, ValueError):
        # Attribute error if the six module isn't what it should be and doesn't
        # have a .__version__; ValueError if the version string exists but is
        # somehow bogus/unparseable
        continue
else:
    raise ImportError(
        "Vispy requires the 'six' module of minimum version {0}; "
        "normally this is bundled with the astropy package so if you get "
        "this warning consult the packager of your Vispy "
        "distribution.".format(_SIX_MIN_VERSION))

if PY3:
    file_types = (io.TextIOWrapper, io.BufferedRandom)
else:
    file_types = (file, io.TextIOWrapper, io.BufferedRandom)
