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

'''
    Defines common unix utilities as Command classes.

    This is mostly a stripped-down list of utilities provided by busybox,
    with some additions. Utilities that could do permanent unintentional
    damage or duplicate with complete overlap functionality that exists
    in python builtins or standard libraries were intentionally omitted.
'''

__author__ = 'Will Leszczuk'

from core import Command

class addgroup(Command): pass
class adduser(Command): pass
class ar(Command): pass
class arp(Command): pass
class arping(Command): pass
class awk(Command): pass
class basename(Command): pass
class blkid(Command): pass
class bunzip2(Command): pass
class bzip2(Command): pass
class cat(Command): pass
class chattr(Command): pass
class chgrp(Command): pass
class chmod(Command): pass
class chown(Command): pass
class cksum(Command): pass
class cp(Command): pass
class cut(Command): pass
class date(Command): pass
class dc(Command): pass
class df(Command): pass
class diff(Command): pass
class dirname(Command): pass
class du(Command): pass
class echo(Command): pass
class env(Command): pass
class expand(Command): pass
class expr(Command): pass
class false(Command): pass
class find(Command): pass
class fold(Command): pass
class free(Command): pass
class grep(Command): pass
class gunzip(Command): pass
class gzip(Command): pass
class hdparm(Command): pass
class head(Command): pass
class hexdump(Command): pass
class hostid(Command): pass
class hostname(Command): pass
class ifconfig(Command): pass
class ifdown(Command): pass
class ifup(Command): pass
class install(Command): pass
class ip(Command): pass
class kill(Command): pass
class killall(Command): pass
class ln(Command): pass
class ls(Command): pass
class lsattr(Command): pass
class lsmod(Command): pass
class md5sum(Command): pass
class mkdir(Command): pass
class modprobe(Command): pass
class mount(Command): pass
class mv(Command): pass
class netstat(Command): pass
class nice(Command): pass
class patch(Command): pass
class pidof(Command): pass
class ping(Command): pass
class ps(Command): pass
class pwd(Command): pass
class readlink(Command): pass
class realpath(Command): pass
class renice(Command): pass
class rm(Command): pass
class rmdir(Command): pass
class sed(Command): pass
class sendmail(Command): pass
class seq(Command): pass
class sha1sum(Command): pass
class sort(Command): pass
class sync(Command): pass
class sysctl(Command): pass
class tail(Command): pass
class tar(Command): pass
class tee(Command): pass
class time(Command): pass
class touch(Command): pass
class tr(Command): pass
class true(Command): pass
class umount(Command): pass
class uname(Command): pass
class uniq(Command): pass
class unzip(Command): pass
class wc(Command): pass
class which(Command): pass
class xargs(Command): pass
class yes(Command): pass
class zcat(Command): pass
