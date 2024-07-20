# Z. Three Numbers
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z

values = list(map(int,input().split()))

def count_valid_combinations(K, S):
    count = 0
    for X in range(K + 1):
        for Y in range(K + 1):
            Z = S - X - Y
            if 0 <= Z <= K:
                count += 1
    return count

K = values[0]
S = values[1]

print(count_valid_combinations(K, S))


# “The problem asks you to count how many different sets of three numbers X,Y,X, Y,X,Y, and ZZZ exist, where each number is between 0 and KKK, and the sum of X,Y,X, Y,X,Y, and ZZZ equals SSS. 
# For example, if K\=2K = 2K\=2 and S\=3S = 3S\=3, you need to find all combinations of X,Y,X, Y,X,Y, and ZZZ that add up to 3, with each number ranging from 0 to 2.”
