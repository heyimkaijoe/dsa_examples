# Complexity: O(n)
def linear_search(unordered_list, search_value):
    for index in range(len(unordered_list)):
        if unordered_list[index] == search_value:
            return True   
    return False

print(linear_search([1,3,4,5,8], 9)) # False
print(linear_search([1,3,4,5,8], 5)) # True
