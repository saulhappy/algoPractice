# A = [1, -2, -3, 5]
# helper function to return required sign
def getSignOfInt(num):
    if num < 0: return -1
    if num == 0: return 0
    if num > 0: return 1

def solution(A):
    # since array must have at least one element, check if multiplication isn't needed:
    if len(A) == 1:
        return getSignOfInt(A[0])
    if len(A) == 2:
        current_result = A[0] * A[1]
        return getSignOfInt(current_result)
    
    # if array has more than 2 elements, iteration needed:
    current_result = A[0] * A[1]
    for i in range(2, len(A)):
        current_result *= A[i]
    return getSignOfInt(current_result)

print(solution([1, 2, 0, -5]))