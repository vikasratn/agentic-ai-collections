
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test cases
test_lists = [
    [38, 27, 43, 3, 9, 82, 10],
    [],
    [1, 5, 3, 9, 7, 4]
]

sorted_lists = []
for test_list in test_lists:
    merge_sort(test_list)  # Sort the list in place
    sorted_lists.append(test_list)

print("Sorted lists:")
for sorted_list in sorted_lists:
    print(sorted_list)
