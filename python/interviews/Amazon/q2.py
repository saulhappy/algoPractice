def find_group(friends, person):
    stack = []
    stack.append(person)
    group = set()
    group.add(person)
    while stack:
        current = stack.pop()
        for i, neighbor in enumerate(friends[current]):
            if neighbor == 1:
                if i not in group:
                    group.add(i)
                    stack.append(i)
    return group
def count_groups(friends):
    seen = set()
    groups = 0
    # For each person, have we seen them?
    # If not, find all the people in their group
    # If so, skip
    for person in range(len(friends)):  # 0-4
        if person in seen: 
            continue
        else:
            group = find_group(friends, person)  # [0 1 2 4]
            groups += 1
            print(group)
            seen.update(group)
    return groups        
friends = [[1, 1, 0, 0, 1],
           [1, 1, 1, 0, 0],
           [0, 1, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [1, 0, 0, 0, 1]]
friends = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]
friends = [[1, 1, 0],
           [1, 1, 0],
           [0, 0, 1]]
print(count_groups(friends))
#print(find_group(friends, 0))
