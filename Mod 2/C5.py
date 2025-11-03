def perm_recur(ele):
    if len(ele) == 0:
        return []
    if len(ele) == 1:
        return [ele]

    result = []
    for i in range(len(ele)):#len[ele]=5, 0->4
        cur_ele = ele[i]#ele[1]
        rem_ele = ele[:i] + ele[i+1:]#[strt:stop:step]=> ele[:i]+ele[i+1]=>ele[1]([1])+ele[5]([3,4,5])
        
        for p in perm_recur(rem_ele):#rem_ele is a list
            result.append([cur_ele] + p)
            
    return result
def brute_force_assignment(cost_matrix):
    n = len(cost_matrix)
    
    jobs = list(range(n)) 
    
    min_cost = float('inf')
    best_assignment = []

    all_assignments = perm_recur(jobs)

    for p in all_assignments:
        curr_cost = 0
        
        for i in range(n):
            job_index = p[i]
            cost = cost_matrix[i][job_index]
            curr_cost += cost
        
        if curr_cost < min_cost:
            min_cost = curr_cost
            best_assignment = p[:]
            
    return min_cost, best_assignment


COST_MATRIX_3X3 = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

min_cost, assignment = brute_force_assignment(COST_MATRIX_3X3)

print("The min cost is: ",min_cost)
print("The best assignment is:",assignment)
