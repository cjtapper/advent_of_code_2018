#!/usr/bin/env python3
import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

twos = 0
threes = 0

with open(args.input_file) as f:

    for line in f:
        count = Counter(line)

        if 2 in count.values():
            twos += 1
        if 3 in count.values():
            threes +=1

checksum = twos * threes
print(checksum)
