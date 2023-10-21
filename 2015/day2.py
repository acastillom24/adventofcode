"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""

# Carga de los datos
path_data = "./day2.txt"
lines = []

with open(path_data) as f:
    for l in f:
        line = l.strip()
        line = line.split("x")
        lines.append(line)

total = 0

for el in lines:
    length_width = float(el[0]) * float(el[1])
    width_height = float(el[1]) * float(el[2])
    height_length = float(el[2]) * float(el[0])

    if (
        width_height <= length_width <= height_length
        or width_height <= height_length <= length_width
    ):
        extra = width_height
    elif (
        length_width <= width_height <= height_length
        or length_width <= height_length <= width_height
    ):
        extra = length_width
    else:
        extra = height_length

    total += 2 * length_width + 2 * width_height + 2 * height_length + extra

print(total)

"""
--- Part Two ---
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
"""

# Carga de los datos
path_data = "./day2.txt"
lines = []

with open(path_data) as f:
    for l in f:
        line = l.strip()
        line = line.split("x")
        lines.append(line)

total = 0

for el in lines:
    length_width = float(el[0])
    width_height = float(el[1])
    height_length = float(el[2])

    regalo = length_width * width_height * height_length

    if (
        length_width <= width_height <= height_length
        or width_height <= length_width <= height_length
    ):
        extra = 2 * (length_width + width_height)

    if (
        height_length <= length_width <= width_height
        or length_width <= height_length <= width_height
    ):
        extra = 2 * (height_length + length_width)
    if (
        width_height <= height_length <= length_width
        or height_length <= width_height <= length_width
    ):
        extra = 2 * (width_height + height_length)

    total += regalo + extra

print(total)
