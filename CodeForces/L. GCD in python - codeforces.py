# L. GCD
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/L

values = list(map(int, input().split()))
newlist = []

for i in range(1, min(values[0], values[1]) + 1):
    if values[0] % i == 0 and values[1] % i == 0:
        newlist.append(i)

print(max(newlist))
