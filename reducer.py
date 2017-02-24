#!/usr/bin/env python

from operator import itemgetter
import sys

current_age = None
current_count = 0
count=1
age = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    age, val = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        val = float(val)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_age == age:
        current_count += count
        avg_add+=val
    else:
        if current_age:
            # write result to STDOUT
            avg=avg_add/current_count
            print '%s\t%s' % (current_age, avg)
            count=1
        current_count = count
        current_date = date
        avg_add=val

# do not forget to output the last word if needed!
if current_age == age:
    print '%s\t%s' % (current_age, avg)