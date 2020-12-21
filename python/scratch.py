# my_dict = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }

# my_dict[4] = 'd'

# print(my_dict)

# normal recursive + memo:

n = 38
def fibonnaci_rec_memo(n):
    memo = {
        0 : 0,
        1 : 1, 
        2 : 1
    }

    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    elif n in memo.keys():
        return memo[n]
    else:
        result = fibonnaci_rec_memo(n - 1) + fibonnaci_rec_memo(n - 2)
        memo[n] = result
        return result


print(fibonnaci_rec_memo(n))