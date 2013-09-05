#!/usr/bin/env python

import os
import sys
import time

# When the parent dies we are seeing continual newlines, so we only access so many before stopping
counter = 0

while True:
	try:
		line = sys.stdin.readline().strip()
		if line == "":
			counter += 1
			if counter > 100:
				break
			continue

		counter = 0

		print >> sys.stderr, '-'*80, '\n', line, '\n', '-'*80
	except KeyboardInterrupt:
		pass
	except IOError:
		# most likely a signal during readline
		pass