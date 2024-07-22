# G. Factorial
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/G

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    T = int(input("Enter the number of test cases: "))
    test_cases = []
    
    for _ in range(T):
        n = int(input("Enter a number: "))
        test_cases.append(n) # here it stores the values I input, in the example it stores [5,3]
    
    results = [factorial(n) for n in test_cases]
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
