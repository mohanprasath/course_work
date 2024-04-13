
magicians = ['Qunetin', 'Julia', 'Alice', 'Josh']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, thats was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")
print("Thank you, everyone. Thats was a great trick!")

# avoid indentation errors - mostly non-existent in modern GUI Editors
# don't forget to indent the lines properly, and the consecutive lines
# logical errors are preventable
# avoid unnecessary indents
# syntax errors - missing the colon :

# try it yourself
pizzas = ['margarita', 'mozzarella', 'stone-baked salmon salami']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

for i in range(5):
    print(i)

print(list(range(2, 21, 2)))

squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
print(squares)

# min, max, sum
# list comprehension
l = [i for i in range(100)]
print(l)

# print(list(range(10000000)))
# print(sum(range(100000000)))

print([l for l in range(1, 101, 2)])
print([i for i in range(3, 300, 3)])

for i in range(10):
    print(i**3)
print([i**3 for i in range(10)])

# copying
my_foods = ['pizza', 'cheese', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # slice copy
print(friend_foods)
my_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# try it yourself
print(f"The first three items in the list are {my_foods[:3]}")
print(f"The last three items in the list are {my_foods[-4:-1]}")
print(f"The middle three items in the list are {my_foods[1:4]}")

my_foods.append('peanut butter')
friend_foods.append('tahini')
print(f"My foods are {my_foods}")
print(f"My friend foods are {friend_foods}")

# tuples
'''
immutable
items in square braces []
declared in ()
normal for in looping over items
'''
food_offers = ('pizza', 'pasta', 'cheese', 'falafel', 'salads')
print(food_offers)
print(type(food_offers))
food_offers = ('pizza', 'pasta', 'cheese', 'falafel', 'mediterranian salads')
print(food_offers)

'''
Code Styling

PEP 8 standards

indentation - four spaces indentation (?) richard spaces vs tabs
line length - 80 (79 default for normal computer window size), comments to 72 characters per line
in the end, line length depends on team and 'the' project person
'''