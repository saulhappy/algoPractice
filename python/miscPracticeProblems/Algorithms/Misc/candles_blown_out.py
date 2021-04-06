"""
From Karat practice interview

"""


hallway1 = ['.','.','>','.','i','i','.']
hallway2 = ['i','>','.','i','.','i','.']
hallway3 = ['i','.','<','.','.','.','.']
hallway4 = ['.','i','<','i','.','.','.']
hallway5 = ['<','i','i','i','i']
hallway6 = ['i','i','i','i','>']


def candles_blown_out (hallway):
    candles = 0
    for i in range(len(hallway)):
        if hallway[i] == '>':
            for j in range(i+1, len(hallway)):
                if hallway[j] == 'i':
                    candles += 1
        if hallway[i] == '<':
            for j in range(i):
                if hallway[j] == 'i':
                    candles +=1 
    
    return candles


    
    
print(candles_blown_out(hallway6))