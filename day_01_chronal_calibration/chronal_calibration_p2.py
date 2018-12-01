#!/usr/bin/env python3
import argparse
from itertools import cycle

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

freq = 0
seen = set([0])

with open(args.input_file, 'r') as f:
    for line in cycle(f):
        freq += int(line)
        if freq in seen:
            print(freq)
            exit()
        seen.add(freq)
