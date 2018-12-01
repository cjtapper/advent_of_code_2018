#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

freq = 0

with open(args.input_file, 'r') as f:
    for line in f:
        freq += int(line)

print(freq)
