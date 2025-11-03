def MakeArrangements(items, current, taken):
    m = len(items)

    
    if len(current) == m:
        print(current)
        return


    for k in range(m):
        if not taken[k]:
            taken[k] = True
            current.append(items[k])

            MakeArrangements(items, current, taken)

            current.pop()
            taken[k] = False



items = ['A', 'B', 'C']
taken = [False] * len(items)

MakeArrangements(items, [], taken)
