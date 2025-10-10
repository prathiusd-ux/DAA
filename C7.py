
# 7
import time


def bubble_sort(data):
    operation_count = 0
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            operation_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                operation_count += 1
    return operation_count


def insertion_sort(data):
    operation_count = 0
    n = len(data)
    for i in range(1, n):
        current_value = data[i]
        j = i - 1
        while j >= 0 and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1
            operation_count += 1
        data[j + 1] = current_value
        operation_count += 1
    return operation_count


def clone_array(source):
    return source.copy()


def main():
    n = int(input("Enter number of elements: "))
    numbers = []
    print("Enter " + str(n) + " elements:")
    for _ in range(n):
        numbers.append(int(input()))

    

    # Bubble Sort
    temp_data = clone_array(numbers)
    start_time = time.time()
    bubble_ops = bubble_sort(temp_data)
    end_time = time.time()
    print("--- Bubble Sort ---")
    print("Time: " + str(end_time - start_time) + " seconds")
    print("Operations: " + str(bubble_ops))
    print("Memory: " + str(temp_data.__sizeof__()) + " bytes")

    # Insertion Sort
    temp_data = clone_array(numbers)
    start_time = time.time()
    insertion_ops = insertion_sort(temp_data)
    end_time = time.time()
    print("\n--- Insertion Sort ---")
    print("Time: " + str(end_time - start_time) + " seconds")
    print("Operations: " + str(insertion_ops))
    print("Memory: " + str(temp_data.__sizeof__()) + " bytes")

if __name__ == "__main__":
    main()
