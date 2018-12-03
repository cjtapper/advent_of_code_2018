import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
args = parser.parse_args()

LENGTH = WIDTH = 1000

fabric = np.zeros((LENGTH, WIDTH), dtype=int)
count = 0

with open(args.input_file) as f:
    for line in f:
        id_ = int(line.split('@')[0].split('#')[1].strip())
        x, y = [int(a) for a in line.split('@')[1].split(':')[0].strip().split(',')]
        w, h = [int(a) for a in line.split(':')[1].strip().split('x')]

        for row in range(y, y+h):
            for col in range(x, x+w):
                if not fabric[row][col]:
                    fabric[row][col] = id_
                elif fabric[row][col] != -999:
                    fabric[row][col] = -999
                    count += 1

print(count)

