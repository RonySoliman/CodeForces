# two-pointers

a = [1, 3, 5, 8, 10]
b = [2, 6, 7, 9, 13]
c = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# If there are remaining elements in `a` or `b`, add them to `c`
while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)

# [1, 2, 3, 5, 6, 7, 8, 9, 10, 13]
