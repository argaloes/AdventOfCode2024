#Advent of Code Day 1
import numpy as np

#pt 1-----

a = []
b = []

with open("input.txt", "r") as file:
    for line in file:
        temp = line.split()
        a.append(int(temp[0]))
        b.append(int(temp[1]))

a = np.sort(a)
b = np.sort(b)

c = abs(np.subtract(a, b))
total_distance = np.sum(c)

print(total_distance)

#part 2-----

keyset = set(a)
b_occurrence = {key: np.count_nonzero(b == key) for key in keyset}

d = []
i = 0
while i < len(a):
    d.append(a[i] * b_occurrence[a[i]])
    i += 1

similarity_score = np.sum(d)

print(similarity_score)
