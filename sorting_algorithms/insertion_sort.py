def insertion_sort(list):
    '''
        Time complexity:
               Best: Ω(n) -> already sorted
              Worst: O(n^2) -> in reverse order
            Average: Θ(n^2)
        Space complexity:
            O(1) -> in-place algorithm
        Stability:
            stable algorithm
    '''
    
    res = [list[:]]

    for i in range(len(list)):
        j = i - 1

        while j >= 0 and (list[j] > list[j + 1]):
            list[j], list[j + 1] = list[j + 1], list[j]
            res.append(list[:])
            j -= 1
    
    return res

print(insertion_sort([3, 8, 7, 9, 4])) # [[3, 8, 7, 9, 4], [3, 7, 8, 9, 4], [3, 7, 8, 4, 9], [3, 7, 4, 8, 9], [3, 4, 7, 8, 9]]
