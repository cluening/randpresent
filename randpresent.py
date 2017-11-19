#!/usr/bin/python

import random
import operator
import math
import os
from datetime import datetime

def fib(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a

import forecastio
api_key = os.environ['APIKEY']
nums = {
  "Ryan": forecastio.load_forecast(api_key, -77.8445, 166.6696).currently().temperature + 273.15,
  "Cory": math.pi,
  "Quentin": 44,
  "Kelcey": 8409,
  "Lis": 51.2,
  "Liz": 43,
  "Alisha": 123115,
  "Alicia": 92384,
}

nums2016 = {"Ryan": 13579,
        "Cory": 2.5,
        "Lis": 987654321,
        "Quentin": 26,
        "Liz": 4343,
        "Kelcey": 1}

nums2015 = {"Ryan":    0,
        "Cory":    849380234,
        "Quentin": fib(346),
        "Kelcey":  1145524,
        "Lis":     8.6271}

nums2014 = {"Ryan":     os.getpid(),
        "Cory":     5056951313,
        "Jenny":    320, # Too lazy to write a function to calculate phi(820); just using the value from an online calculator
        "Lis":      1,
        "Quentin":  73,
        "Kelcey":   5524}

nums2013 = {"Ryan":     math.log(22507.2),
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
