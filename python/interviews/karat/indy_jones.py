"""
While exploring an ancient tomb for treasure, you've come across a room with strange symbols on the floor. These symbols tell you which way you need to walk in order to pass through the room. However, you're not certain whether it's possible to follow these directions and reach the end of the room.

You will be given a grid of symbols like the following:

(start here --->)  >   >   >   >   v
                   v   ^   >   ^   v
                   >   ^   ^   >   E

You start on the square in the upper left, and need to reach the square marked "E". From each square you must follow the direction on the square. The directions are as follows:

 v : move down
 > : move right
 ^ : move up
 < : move left

In this case, you can reach the end square:

  [>] [>] [>] [>] [v]
   v   ^   >   ^  [v]
   >   ^   ^   >  [E]

However, the symbols may lead you off the edge.

  Right: off edge
   [>] [>] [v]
    v   ^  [>]
    <   >   E

Also, the end may not be at the bottom right.

 [>] [>] [v] [E]  v
  v   ^  [>] [^]  v
  >   ^   ^   >   >

The path is guaranteed not to loop.

Write a function that determines if it is possible to reach the end of the room from the start position in the upper left.

All Test Cases:
forced_march(floor1)   => True
forced_march(floor2)   => False
forced_march(floor3)   => True
forced_march(floor4)   => True
forced_march(floor5)   => False
forced_march(floor6)   => True
forced_march(floor7)   => False
forced_march(floor8)   => False
forced_march(floor9)   => True
"""


def forced_march(floor):
    # directions = {
    #     """TODO"""
    #     ">": (0, 1),
    # }
    
    # row = 0
    # column = 0
    
    # if floor[row][column] == 'E':
    #     return true
    # else:
    #     directions[]
        

floor1 = [
    ['>', '>', '>', '>', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', '^', '^', '>', 'E']
]

floor2 = [
    ['v', '>', 'v'],
    ['v', '^', '>'],
    ['<', '>', 'E']
]

floor3 = [
    ['v', '>', '>', 'v', '>'],
    ['>', '>', 'v', '>', '^'],
    ['^', '>', '>', '>', 'E']
]

floor4 = [
    ['v', '>', '>', 'v'],
    ['v', '^', '>', '>'],
    ['v', '>', '>', 'v'],
    ['v', '^', '<', 'v'],
    ['>', '>', '^', 'E']
]

floor5 = [
    ['>', '>', '>', '>', '>', '>', '>', '>', '>', 'v'],
    ['v', '^', '>', 'v', '<', '>', 'v', '<', '<', '<'],
    ['>', '^', 'v', '<', '^', '<', '<', '^', '>', 'E']
]

floor6 = [
    ['>', '>', 'v', 'E', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', '^', '^', '>', '>']
]

floor7 = [
    ['>', '>', 'v', '>', 'v'],
    ['v', '^', '>', '^', 'v'],
    ['>', 'E', '^', '>', '>']
]

floor8 = [
    ['>', '>', 'v', '>', '^'],
    ['v', '^', '>', '^', 'v'],
    ['>', 'E', '^', '>', '>']
]

floor9 = [
    ['>', 'v', '>', '>', 'v', '^'],
    ['v', '<', '^', 'v', '<', 'E'],
    ['>', '>', '^', '>', '>', '^']
]
