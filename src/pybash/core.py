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

''' core abstractions for providing bash-like scripting blocks in python '''

__author__ = 'Will Leszczuk'

import commands

class __MetaCommand(type):
    def __getitem__(cls, item):
        return cls()[item]

    def __str__(cls):
        return str(cls())

    def __or__(cls, other):
        return cls() | other

    def __sub__(cls, other):
        return cls() - other


class Command(object):
    __metaclass__ = globals()['__MetaCommand']
    
    def __init__(self, *args):
        self.command = repr(self.__class__).split('.')[-1].split("'")[0]
        if 0 != len(args):
            self.command += ' %s' % ' '.join(str(a) for a in args)

    def __call__(self, *args):
        if 0 != len(args):
            self.command += ' %s' % ' '.join(str(a) for a in args)
        return self

    def __getitem__(self, item):
        if type(item) == slice:
            self.command += ' -%s %s' % (str(item.start), str(item.stop))
        else:
            self.command += ' -%s' % item

        return self

    def __or__(self, other):
        self.command += ' | %s' % str(other)
        return self

    def __sub__(self, other):
        self.command += ' -%s' % str(other)
        return self

    def __str__(self):
        return self.command

    
class __MetaFlag(type):
    def __str__(cls):
        return str(cls())

    def __getitem__(cls, item):
        return cls()[item]

    
class Flag(object):
    __metaclass__ = globals()['__MetaFlag']
    
    def __init__(self, *args):
        self.command = repr(self.__class__).split('.')[-1].split("'")[0]
        if 0 != len(args):
            self.command += ' %s' % ' '.join(str(a) for a in args)

    def __getitem__(self, item):
        if type(item) == slice:
            self.command += ' -%s %s' % (str(item.start), str(item.stop))
        else:
            self.command += ' -%s' % item

        return self

    def __str__(self):
        return self.command
    

class ShellError(Exception):
    def __init__(self, cmd, exitcode, output):
        Exception.__init__(
            self,
            'Command [%s] returned exit code [%d] (output = [%s])' %
                (cmd, exitcode, output)
        )

        
class Shell(object):
    def __init__(self, failfast=False):
        self.failfast = failfast
        self.exitcode = 0

    def __call__(self, cmd):
        cmd = str(cmd)
        status, output = commands.getstatusoutput(cmd)
        if self.failfast and status != 0:
            raise ShellError(cmd, status, output)
        self.exitcode = status
        return output
