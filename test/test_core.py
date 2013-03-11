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

''' functional test harness for pysh project '''

__author__ = 'Will Leszczuk'

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from pybash.utils import awk, find, grep, ls, ps
from pybash.flags import l, A, v, C1, lA, aux, name, maxdepth

class TestCommandConstruction(unittest.TestCase):
    def test_one_command(self):
        self.assertEqual('ls', str(ls))

    def test_one_command_instance(self):
        self.assertEqual('ls', str(ls()))

    def test_one_arg(self):
        self.assertEqual('ls /tmp', str(ls('/tmp')))

    def test_brace_param(self):
        self.assertEqual('ls -lA', str(ls[lA]))

    def test_brace_param_called(self):
        self.assertEqual('ls -lA', str(ls[lA]()))

    def test_brace_param_and_arg(self):
        self.assertEqual('ls -lA /tmp', str(ls[lA]('/tmp')))

    def test_two_brace_params_and_arg(self):
        self.assertEqual('ls -l -A /tmp', str(ls[l][A]('/tmp')))

    def test_param_with_value(self):
        self.assertEqual('ls -I will', str(ls['I':'will']))

    def test_param_with_numeric_value(self):
        self.assertEqual('ls -I 1', str(ls['I':1]))

    def test_command_with_params_piped_to_command_with_args(self):
        self.assertEqual('ls -lA | grep will', str(ls -lA | grep('will')))

    def test_command_piped_to_command_with_brace_params(self):
        self.assertEqual('ls | grep -v vcap', str(ls | grep[v:'vcap']))

    def test_command_with_brace_params_piped_to_command_with_brace_params(self):
        self.assertEqual('ls -lA | grep -v vcap', str(ls[lA] | grep[v:'vcap']))

    def test_command_with_params_and_args_piped_to_same(self):
        self.assertEqual(
            'ls -lA /tmp | grep -v orbit',
            str(ls -lA ('/tmp') | grep -v ('orbit'))
        )

    def test_command_with_two_params_piped_to_command_with_arg(self):
        self.assertEqual('ls -l -A | grep .pyc', str(ls -l -A | grep ('.pyc')))

    def test_multiple_pipes(self):
        self.assertEqual(
            "ps -aux | grep bash | awk '{print $2}'",
            str(ps -aux | grep ('bash') | awk ("'{print $2}'"))
        )

    def test_command_piped_to_command_with_multiple_params(self):
        self.assertEqual(
            'ls | grep -v flags -C1',
            str(ls | grep -v('flags') -C1)
        )

    def test_mixed_param_arg_syntax(self):
        self.assertEqual(
            'find / -maxdepth 1 -name proc',
            str(find('/') -maxdepth(1) -name('proc'))
        )

    def test_multiple_arg_multiple_call_syntax(self):
        self.assertEqual('ls / /home', str(ls('/')('/home')))

    def test_multiple_arg_single_call_syntax(self):
        self.assertEqual('ls / /home', str(ls('/', '/home')))

        
if '__main__' == __name__:
    unittest.main()
