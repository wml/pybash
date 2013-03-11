#!/usr/bin/python

# Copyright (c) 2013 William Leszczuk
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

''' distutils installation script for pybash '''

__author__ = 'Will Leszczuk'

from distutils.core import setup

setup(name = "pybash",
    version = "1.0",
    description = "a library for unifying bash and python systems programming",
    author = "Will Leszczuk",
    # TODO: WML: dedicated address for these
    #   author_email = "email@someplace.com",
    url = "http://github.com/wml/pybash",
    packages = ['pybash'],
    package_dir = {'pybash' : 'src/pybash' },
    scripts = [],
    # long_description = """Really long text here.""" 
) 
