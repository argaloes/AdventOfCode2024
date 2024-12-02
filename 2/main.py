import numpy as np

#part 1 -----

a = []
b = []

with open("input.txt", "r") as file:
    for line in file:
        a = np.array([int(x) for x in line.split()])
        a_asc = np.sort(a)
        a_des = np.sort(a)[::-1]

        if ((a == a_asc).all() or (a == a_des).all()):
            if (all(1 <= (abs(a1 - a2)) <= 3 for a1, a2 in zip(a, a[1:]))):
                b.append("Safe")
            else:
                b.append("Unsafe")
        else:
            b.append("Unsafe")

c = b.count("Safe")
print(c)

#part 2 -----

a = []
b = []

def red_nose(a):
    a_asc = np.sort(a)
    a_des = np.sort(a)[::-1]

    if ((a == a_asc).all() or (a == a_des).all()):
        if(all(1 <= (abs(a1 - a2)) <= 3 for a1, a2 in zip(a, a[1:]))):
            return True

with open("input.txt", "r") as file:
    for line in file:
        a = np.array([int(x) for x in line.split()])

        if (red_nose(a)):
            b.append("Safe")
        elif (any(red_nose(np.concatenate([a[:i], a[i+1:]])) for i in range(len(a)))):
            b.append("Safe")
        else:
            b.append("Unsafe")

c = b.count("Safe")
print(c)


