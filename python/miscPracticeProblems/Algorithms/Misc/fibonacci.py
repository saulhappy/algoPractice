""" return nth number of fibonnaci sequence """

fib_sequnce = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]


# normal recursive:

def fibonnaci_rec(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci_rec(n - 1) + fibonnaci_rec(n - 2)

print(fib_sequnce[28])
print(f"fib of 28 is {fibonnaci_rec(28)}")
