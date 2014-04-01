#!/usr/bin/python

import random
import operator
import math
from datetime import datetime

nums = {"Ryan":     math.log(22507.2),
        "Cory":     88,
        "Jenny":    2,
        "Lis":      (lambda x: ((x.microseconds + (x.seconds + x.days * 24 * 3600) * 10**6) / 10**6) / (365.0*24.0*60.0*60.0))(datetime.now() - datetime.strptime("04/15/09 8:23", "%m/%d/%y %H:%M")),
        "Quentin":  42,
        "Kelcey":   13}

nums2012 = {"Ryan":     316.5, 
	"Cory":     154786, 
	"Jenny":    8675309,
	"Lis":      4578801264289633, 
	"Quentin":  42, 
	"Kelcey":   4812}

nums2011 = {"Ryan":     42,
        "Cory":     math.e,
        "Lis":      math.sqrt(196)+3,
        "Quentin":  7732,
        "Kelcey":   11/4}

random.seed()
names = nums.keys()
random.shuffle(names)
print names
print nums

sortednums = sorted(nums.iteritems(), key=operator.itemgetter(1))
print sortednums

dup = False
for i in range(0, len(names)):
  if names[i] == sortednums[i][0]:
    dup = True

if dup == False:
  print "Final assignments:"
  for i in range(0, len(names)):
    print "%s -> %s" % (names[i], sortednums[i][0])
else:
  print "Duplicates.  Try again!"