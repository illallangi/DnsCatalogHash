#!/usr/bin/env python

import dns.name
import hashlib
import sys

print (sys.argv[1] + ' ' + (hashlib.sha1(dns.name.from_text(sys.argv[1]).to_wire()).hexdigest()))
