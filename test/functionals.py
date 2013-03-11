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

''' pybash functional tests. '''

__author__ = 'Will Leszczuk'

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from pybash.core import Shell

# Histogram imports
from pybash.utils import awk, echo, sed, sort, tr, uniq
from pybash.flags import c, r

# Checksum imports
from pybash.utils import cksum, find
from pybash.flags import maxdepth, name

HistogramFileContent = '''\
This is a file with many words.
The words may be upper- or lower-case.
However, punctuation should not be counted.\
'''

# 3876287687 5 /tmp/f1.txt
ChecksumFile1Content = 'abcd\n'
ChecksumFile1Name = '/tmp/f1.txt'

# 128431099 14 /tmp/f2.txt
ChecksumFile2Content = 'bunch of data\n'
ChecksumFile2Name = '/tmp/f2.txt'

class TestHistogram(unittest.TestCase):
    def test_histogram(self):
        sh = Shell(failfast=True)
        answer = sh(
            echo('"%s"' % HistogramFileContent.lower()) | tr("' '", "'\n'") |
                sed(r"'s/\W//g'") | sort | uniq -c | sort |
                sed(r"'s/^\s\+//g'")
        )
        
        self.assertEqual('''\
1 a
1 counted
1 file
1 however
1 is
1 lowercase
1 many
1 may
1 not
1 or
1 punctuation
1 should
1 the
1 this
1 upper
1 with
2 be
2 words\
''',
            answer
        )


class TestDirectoryChecksum(unittest.TestCase):    
    def test_directory_checksum(self):
        with open(ChecksumFile1Name, 'w') as out:
            out.write(ChecksumFile1Content)

        with open(ChecksumFile2Name, 'w') as out:
            out.write(ChecksumFile2Content)
            
        sh = Shell(failfast=True)
        actual = sh(
            find ('/tmp') [maxdepth:1] [name:"'f?.txt'"] ['exec':'cksum {} \\;']
                | cksum
        )

        self.assertEqual('4207455888 50', actual)


if __name__ == '__main__':
    unittest.main()
