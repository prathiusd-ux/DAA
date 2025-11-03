def Comb(items, start_index, current_combo, k):
    
    if len(current_combo) == k:
        print(current_combo)
        return

    
    for i in range(start_index, len(items)):
        current_combo.append(items[i])
        Comb(items, i + 1, current_combo, k)
        current_combo.pop()  


# Example usage
ele = ['A', 'B', 'C', 'D']
k = 2  
Comb(ele, 0, [], k)
