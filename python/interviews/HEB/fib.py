# Fibonacci Series
# Programming challenge description:
# The Fibonacci series is defined as F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) where n>1. Given a positive integer n, print the value of F(n).
# Input:
# Your program should read lines of text from standard input. Each line will contain a single positive integer, n.
# Output:
# For each input n, print to standard output the fibonacci number, F(n), one per line.
# Test 1
# Test Input
# Download Test 1 Input
# 5
# Expected Output
# Download Test 1 Input
# 5
# Test 2
# Test Input
# Download Test 2 Input
# 12
# Expected Output
# Download Test 2 Input
# 144

n = 12

def F(n, memo = {}):
    if n in memo.keys():
        return memo[n]
    
    if n == 0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        memo[n] = F(n-1, memo) + F(n-2, memo)
        return memo[n]

print(F(5))
print(F(n))
# => 5
# => 144