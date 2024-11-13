import random
import time

# Phase 1: Data Generation and Insertion Sort
def generate_sorted_data(size):
    data = [random.randint(1, 100) for _ in range(size)]  # Generate random integers between 1 to 100
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:  # Shift elements greater than key to the right
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key  # Place the key in the correct position
    return data

# Phase 2: Binary Search
def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if sorted_array[mid] == target:
            return mid  # Return index if the target is found
        elif sorted_array[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half
    return None  # Returns none if target not found

# Phase 3: Merge Sort for Large Datasets
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)  # Sorting the left half with recursion
        merge_sort(right_half)  # Sorting the right half with recursion

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Phase 4: Linear Search
def linear_search(array, target):
    for i in range(len(array)):  # Loop to find the target
        if array[i] == target:
            return i  # Return index if target is found
    return None  # Returns none if target not found


def main():
    print("Phase 1: Generating and Sorting Data with Insertion Sort")
    array_size = random.randint(5, 50)  # Random size between 5 and 50
    sorted_data = generate_sorted_data(array_size)
    print("Array size:", array_size)
    print("Sorted Data:", sorted_data)

    print("\nPhase 2: Binary Search")
    target = 29  # target to search for
    index = binary_search(sorted_data, target)
    if index is not None:
        print(f"Target {target} found at index {index}")
    else:
        print(f"Target {target} not found")

    print("\nPhase 3: Sorting Large Data with Merge Sort")
    large_data = [random.randint(1, 100) for _ in range(1000)]  # Large dataset of size 1000
    merge_sort(large_data)
    print("First 10 elements after merge sort:", large_data[:10])

    print("\nPhase 4: Comparing Search Performance")
    target = 72  # target for performance comparison

    # Timing check for linear search
    start_time = time.perf_counter()
    linear_search_result = linear_search(large_data, target)
    end_time = time.perf_counter()
    print(f"Linear search time: {end_time - start_time} seconds")

    # Timing check for binary search
    start_time = time.perf_counter()
    binary_search_result = binary_search(large_data, target)
    end_time = time.perf_counter()
    print(f"Binary search time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

