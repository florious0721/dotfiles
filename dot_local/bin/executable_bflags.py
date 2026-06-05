#!/bin/python

import sys
import os
from subprocess import call as run

cflags = {
    'base': ['-pipe'],
    'dbg': ['-Og', '-g'],
    'release': ['-DNDEBUG'],
    'g': ['-march=x86-64-v2', '-mtune=generic', '-O3'],
    'n': ['-march=native', '-mtune=native', '-O3'],
    'h': [
        '-D_FORTIFY_SOURCE=2',
        '-ftrivial-auto-var-init=zero',
        '-Wl,-z,now', '-Wl,-z,relro',
        '-fstack-protector', '-fstack-clash-protection',
        '-fcf-protection',
    ],
}
ldflags = {
    'base': ['-Wl,-O3', '-Wl,--as-needed', '-Wl,--sort-common'],
    'h': ['-Wl,-z,relro', '-Wl,-z,now']
}

req: set = {'base'}
req.update(set(sys.argv[1].split(sep=',')))
cfenv = os.environ['CFLAGS'] if 'CFLAGS' in os.environ else str()
lfenv = os.environ['LDFLAGS'] if 'LDFLAGS' in os.environ else str()

for i in req:
    if i in cflags:
        cfenv += ' '
        cfenv += ' '.join(cflags[i])
    else:
        print('{} is not set in cflags.'.format(i), file=sys.stderr)
    if i in ldflags:
        lfenv += ' '
        lfenv += ' '.join(ldflags[i])
    else:
        print('{} is not set in ldflags.'.format(i), file=sys.stderr)


os.environ['CFLAGS'] = cfenv
os.environ['CXXFLAGS'] = cfenv
os.environ['LDFLAGS'] = lfenv
print(os.environ['CFLAGS'])
print(os.environ['LDFLAGS'])
exit(run(sys.argv[2:]))
