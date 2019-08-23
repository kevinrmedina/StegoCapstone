#!/usr/bin/env python3

import re
import sys

searchTerm = sys.argv[1]
hexDump = sys.argv[2]

file = open(hexDump, "r")

dumpString = file.read()

lineFromSearch = re.search("", dumpString)
