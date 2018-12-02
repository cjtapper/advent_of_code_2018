#!/usr/bin/env python3
import argparse
from collections import Counter
from itertools import combinations

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

twos = 0
threes = 0

with open(args.input_file) as f:
    box_ids = f.readlines()

box_ids = [b.strip() for b in box_ids]

for a, b in combinations(box_ids, 2):
    common = ''
    count = 0
    for i, j in zip(a,b):
        if i != j:
            count +=1
        else:
            common += i

        if count > 1:
            break

    if count == 1:
        print(common)
