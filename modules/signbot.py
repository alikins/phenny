#!/usr/bin/env python
"""
signbot.py - Phenny Ping Module
Author: blargh
About: http://blargh
"""

import random
import string
import modules.sign

def sign(phenny, input): 
   #phenny.say(input.nick + '!')
   sign = modules.sign.Sign("/dev/ttyS1")
   foo = input.split()
   print "ledsign says: %s" % input
   sign.show(string.join(foo[2:],' '), color="mix", mode="auto")

   
sign.commands = ['sign']
sign.rule = ('$nick', ['say'], '(.*)')
sign.priority = 'high'
sign.thread = False

if __name__ == '__main__': 
   print __doc__.strip()
