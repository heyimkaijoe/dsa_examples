# Hash Table in Python is called "Dictionary"
# Dictionary with items
my_menu  = {
    'espresso': 8,
    'croissant': 10,
    'sandwich': 15,
}

# Get
print(my_menu['croissant']) # 10
print(my_menu['bread']) # will get an error
print(my_menu.get('bread')) # None

# Get items
print(my_menu.items())

# Get keys
print(my_menu.keys())

# Get values
print(my_menu.values())

# Insert
my_menu['latte'] = 12

# Modify
print(my_menu.get('espresso')) # 8
my_menu['espresso'] = 8.5
print(my_menu.get('espresso')) # 8.5

# Remove a key-value pair / dictionary
del my_menu['latte']

# Iterate
for dish in my_menu:
    print(dish)

for price in my_menu.values():
    print(price)

for dish, price in my_menu.items():
    print('The ' + dish + ' costs $' + str(price))

# Nested dictionary
my_new_menu  = {
    'espresso': {
        'price': 8.5,
        'best_served': 'hot',
    },
    'croissant': {
        'price': 10,
        'best_served': 'warm',
    },
    'sandwich': {
        'price': 15,
        'best_served': 'warm',
    },
}
