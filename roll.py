#!/usr/bin/env python3

# D&D-style dice roller by Valkyrie.
#
# Example usage: ./roll.py 3d8+4

from sys import argv
from numpy import random as rand
import re

for roll in argv[1:]:

    matched = re.match(r'^(\d+)d(\d+)\+?(\d+)?$', roll)

    if matched:
        rolls = int(matched.group(1))
        sides = int(matched.group(2))
        additive = 0

        if matched.group(3) is not None:
            additive = int(matched.group(3))

        out = rand.randint(1, sides, rolls)
        outSum = sum(out) + additive
        print(out, "Total: " + str(outSum))