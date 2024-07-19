# L. GCD
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/L

values = list(map(int, input().split()))
newlist = []

for i in range(1, min(values[0], values[1]) + 1):
    if values[0] % i == 0 and values[1] % i == 0:
        newlist.append(i)

print(max(newlist))

# Debugging:
# min function ensures that I only check potential common divisors up to the smaller of the two input values. This is important because a number greater than the smaller of the two numbers cannot be a divisor of both.
# By adding 1, we ensure that the loop includes the smallest of the two numbers. For example, range(1, 12 + 1) would generate numbers from 1 to 12.
