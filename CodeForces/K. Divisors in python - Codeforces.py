# K. Divisors
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/K

value = int(input())

for i in range(1,value):
    if (value%i) == 0:
        print(i)
print(value)
