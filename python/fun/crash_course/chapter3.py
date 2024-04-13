# List

'''
LIFO
mutable
built-in
dynamic - can grow and shrink
fast when small

'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'hero']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[0].title())
print(bicycles[-1].title())

message = f"My favorite bicycle is {bicycles[-1].title()}"
print(message)

# print everything from the beginning
print(bicycles)
print(bicycles[::-1]) # reversed
print(bicycles.reverse())

names = ['John', 'Smith', 'Narad']
print(names[0], names[1], names[2])
print(f"Hello, {names[0]}!")
print(f"Hello, {names[1]}!")
print(f"Hello, {names[2]}!")

transportation = ['car', 'truck', 'bus', 'motorcycle']
print(transportation)
print(f"I like to own a , {transportation[-1]}!")

# inbuilt
print(transportation.index('bus'))
print(transportation.reverse())
print(transportation)
print(transportation.pop()) # LIFO
print(transportation.sort())
print(transportation.remove('truck'))
print(transportation.remove('bus'))
print(transportation)
transportation.append('bicycle')
transportation.sort()
print(transportation.index('motorcycle'))
print(transportation)
transportation.append('metro')
print(transportation)
del transportation[-1]
print(transportation)

# try it yourself
dinner_list = ['nana', 'papa', 'mama', 'vikki', 'gowtham', 'mira', 'auro']
print(dinner_list)
print(dinner_list.sort())
print(dinner_list)
print(dinner_list.sort(reverse=True))
print(dinner_list)
dinner_list = ['nana', 'papa', 'mama', 'vikki', 'gowtham', 'mira', 'auro']
print("original list is ", dinner_list)
print(sorted(dinner_list))
print("reverse sorted dinner list is ", sorted(dinner_list, reverse=True))
print("The original list again is ", dinner_list)
for entry in dinner_list:
    print(f"Hi {entry.title()}, come join us for dinner today!.")
print(f"{dinner_list[3]} can't make it for dinner today!")
print(dinner_list.remove('vikki'))
print("Updates dinner list is ", dinner_list)
for entry in dinner_list:
    print(f"Hi {entry.title()}, come join us for dinner today!.")
# more the merrier
dinner_list.insert(0, "guppy")
dinner_list.insert(4, "sampurna")
dinner_list.append('vv')
for entry in dinner_list:
    print(f"Hi {entry.title()}, come join us for dinner today!.")
print("sorry only two for today!")
while len(dinner_list) > 2:
    dinner_list.pop()
print("The lucky two invited for dinner today! are ", dinner_list)
del dinner_list[0]
del dinner_list[0]
print(dinner_list)

# try it yourself
locations = ['pondy', 'parai', 'meri', 'silen']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print("original list is ", locations)
locations.reverse() # inplace like sort method
print("reversed list is ", locations)
print("new original list is ", locations)
print(len(locations))
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

dinner_list = ['nana', 'papa', 'mama', 'vikki', 'gowtham', 'mira', 'auro']
for entry in dinner_list:
    print(len(entry), entry)
print(f"Number of dinner guest now is {len(dinner_list)}")

'''
# Knwon errors to avoid
index errors
'''