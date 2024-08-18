def bubble_sort(list):
    # Worst case: O(n^2)
    # Average case: Θ(n^2)
    # Best case: Ω(n^2)

    list_length = len(list)

    for i in range(list_length - 1): # doesn't need to sort the first element
        for j in range(list_length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

def improved_bubble_sort(list):
    # Worst case: O(n^2)
    # Average case: Θ(n^2)
    # Best case: Ω(n)
    
    list_length = len(list)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(list_length - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_sorted = False
        list_length -= 1

    return list

print(bubble_sort([3,1,8,2,4]))   # [1, 2, 3, 4, 8]
print(bubble_sort([9,8,7,6,4,2])) # [2, 4, 6, 7, 8, 9]
print(improved_bubble_sort([3,1,8,2,4]))   # [1, 2, 3, 4, 8]
print(improved_bubble_sort([9,8,7,6,4,2])) # [2, 4, 6, 7, 8, 9]
