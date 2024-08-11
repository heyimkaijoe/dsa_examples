# Complexity: O(log n)
def binary_search(ordered_list, search_value):
    start = 0
    end = len(ordered_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if ordered_list[middle] == search_value:
            return True
        elif ordered_list[middle] < search_value:
            start = middle + 1
        else:
            end = middle - 1
    return False

print(binary_search([1,4,7,9,11,14], 4)) # True
print(binary_search([1,4,7,9,11,14], 8)) # False
