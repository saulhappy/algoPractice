"""
given a target integer, and array of nums, return true/false if any combination of existing numbers in array sum to the target integer.
Seems like the Two Sum problem.

"""

target_num = 7
array = [5, 3, 4, 7] # => true, with 3, 4 and 7
# array = [2, 4] # => false


def canSum(target_num, array):
    memo = {}

    for cur_num in array:
        if cur_num == target_num:
            return True
        if cur_num in memo.values():
            return True
        memo[cur_num] = target_num - cur_num
    return False

print(canSum(target_num, array))
