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

def BRT_TSP(dist_matrix, source):
    min_dist = float('inf')
    best_path = []
    n = len(dist_matrix)

    all_cities = list(range(n))
    cities_visit = [city for city in all_cities if city != source]

    all_city_permutations = perm_recur(cities_visit)

    for permutation in all_city_permutations:
        path = [source] + permutation + [source]
        total_distance = 0

        for i in range(len(path) - 1):
            city_i = path[i]
            city_i_plus_1 = path[i+1]
            
            dist_seg = dist_matrix[city_i][city_i_plus_1]
            total_distance += dist_seg

        if total_distance < min_dist:
            min_dist = total_distance
            best_path = path[:]

    return min_dist, best_path

DISTANCES_5_CITIES = [
    [0, 10, 8, 9, 7],
    [10, 0, 10, 5, 6],
    [8, 10, 0, 8, 9],
    [9, 5, 8, 0, 6],
    [7, 6, 9, 6, 0]
]

STARTING_CITY = 0

shortest_distance, optimal_route = BRT_TSP(DISTANCES_5_CITIES, STARTING_CITY)

print("The shortest path is: ", shortest_distance)
print("The optimal path is: ",optimal_route)