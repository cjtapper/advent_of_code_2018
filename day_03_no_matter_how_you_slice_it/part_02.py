import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

LENGTH = WIDTH = 1000

fabric = np.zeros((LENGTH, WIDTH), dtype=int)
count = 0
no_overlap = set()

with open(args.input_file) as f:
    for line in f:
        id_ = int(line.split('@')[0].split('#')[1].strip())
        x, y = [int(a) for a in line.split('@')[1].split(':')[0].strip().split(',')]
        w, h = [int(a) for a in line.split(':')[1].strip().split('x')]

        no_overlap.add(id_)

        for row in range(y, y+h):
            for col in range(x, x+w):
                if not fabric[row][col]:
                    fabric[row][col] = id_
                elif fabric[row][col]:
                    existing = fabric[row][col]
                    if fabric[row][col] != -999:
                        fabric[row][col] = -999
                        count += 1
                    if id_ in no_overlap:
                        no_overlap.remove(id_)
                    if existing in no_overlap:
                        no_overlap.remove(existing)

print(no_overlap)

