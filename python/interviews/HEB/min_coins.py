# Minimum Coins
# Programming challenge description:
# You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive at. Find the minimum number of coins to arrive at it.
# Input:
# Your program should read lines from standard input. Each line contains a positive integer number which represents the total you have to arrive at.
# Output:
# Print out the minimum number of coins required to arrive at the total.
# Test 1
# Test Input
# Download Test 1 Input
# 11
# Expected Output
# Download Test 1 Input
# 3
# Test 2
# Test Input
# Download Test 2 Input
# 20
# Expected Output
# Download Test 2 Input
# 4

coins = [1, 3, 5]

def min_coins(coins, total):
    if total == 0:
        return 0

    coin_map = {}

    for coin in coins:
        coin_map[coin] = 1
    
    for i in range(1,total+1):
        for coin in coins:
            if i - coin in coin_map:
                if i not in coin_map:
                    coin_map[i] = coin_map[i-coin] +1
                else:
                    coin_map[i] = min(coin_map[i],coin_map[i-coin]+1)

    if total not in coin_map:
        return None
    else:
        return coin_map[total]

print(min_coins(coins, 11))
print(min_coins(coins, 20))
# => 3
# => 4