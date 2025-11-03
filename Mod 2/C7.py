import math

def calculate_distance(pt_a, pt_b):
    coordinate_diff = (pt_a[0] - pt_b[0]) ** 2 + (pt_a[1] - pt_b[1]) ** 2
    result = math.sqrt(coordinate_diff)
    return result

def find_minimum_separation(coordinates):
    count = len(coordinates)
    min_separation = float('inf')

    for index_i in range(count):
        for index_j in range(index_i + 1, count):
            separation = calculate_distance(coordinates[index_i], coordinates[index_j])
            if separation < min_separation:
                min_separation = separation

    return min_separation

data_points = eval(input("enter the list of points:"))
min_separation_value = find_minimum_separation(data_points)
print(min_separation_value)