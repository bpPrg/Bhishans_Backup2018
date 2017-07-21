#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# empty lists
col0, col1, col2 = [], [], []
with open('color.txt') as inf:
    for line in inf:
        parts = line.split()  # split line into parts
        if len(parts) > 1:    # if at least 2 parts/columns
            col0.append(parts[0])
            col1.append(parts[1])
            col2.append(parts[2])

print(col0[0])
print(col1[0])
print(col2[0])
