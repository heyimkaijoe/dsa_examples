# Complexity: O(log n)
# Approach 1
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

# Approach 2 w/ recursion
def binary_search_recursion(ordered_list, search_value):
    list_len = len(ordered_list)

    if list_len == 0:
        return False
    else:
        middle = (list_len) // 2
        
        if ordered_list[middle] == search_value:
            return True
        elif ordered_list[middle] < search_value:
            return binary_search_recursion(ordered_list[middle+1:], search_value)
        else:
            return binary_search_recursion(ordered_list[:middle], search_value)

print(binary_search([1,4,7,9,11,14], 4)) # True
print(binary_search([1,4,7,9,11,14], 8)) # False

print(binary_search_recursion([1,4,7,9,11,14], 4)) # True
print(binary_search_recursion([1,4,7,9,11,14], 8)) # False
