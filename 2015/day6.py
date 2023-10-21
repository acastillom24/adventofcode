"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.
- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
- turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

"""

# Uploaded to data

PATH_FILE = "./day6.txt"

with open(PATH_FILE) as f:
    lines = f.readlines()

f.close()

# Create a matrix

import numpy as np
import re


def turn_off(arr, txt=None):
    pares = [int(el) for el in re.findall("\d+", txt)]
    if len(pares) == 4:
        for idx_row in range(pares[0], pares[2] + 1):
            for idx_col in range(pares[1], 1000):
                if txt.startswith("turn off"):
                    arr[idx_row, idx_col] = 0
                if txt.startswith("turn on"):
                    arr[idx_row, idx_col] = 1
                if txt.startswith("toggle"):
                    if arr[idx_row, idx_col] == 0:
                        arr[idx_row, idx_col] = 1
                    else:
                        arr[idx_row, idx_col] = 0
                if idx_row == pares[2] and idx_col == pares[3]:
                    break

    return arr


arr = np.zeros((1000, 1000))

for _, txt in enumerate(lines):
    arr = turn_off(arr, txt)

print(int(np.sum(arr)))
