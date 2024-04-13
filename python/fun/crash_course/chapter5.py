# if statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'BMW':  # equality checks
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':  # inequality checks
    print('Hold the door!')

# other conditions <, <=, >, >=, ==, !=
if 'telsa' not in cars:
    print("Add tesla too!")

car = 'Tesla'
print('Is car == "Tesla"? I predict True')
print(car == 'Tesla')
print(car == 'Audi')
print(car.lower == 'Tesla')

age = 17
if age >= 18:
    print('You can vote!')
else:
    print('Sorry!, you cannot vote!.')

# bus ticket prices
age = 12
price = 0
if age < 4:
    price = 0
elif age <= 12:
    price = 1.25
elif age > 12:
    price = 2.85
elif age >= 65:
    price = 1.25

print(f"Your ticket costs {price} €")

# multiple if's and if elif else can be used - though very rare in bigger projects
# try it yourself
alien_color = ['green', 'yellow', 'red']
points = 0
color = alien_color[2]
if 'green' in color:
    print("You have earned 5 points.")
    points += 5
elif 'yellow' in color:
    print("You have earned 10 points")
    points += 10
elif 'red' in color:
    print("You have earned 15 points")
    points += 15
print(f"Your total is {points} points.")

# stages of life - if elif else
age = 27
if age <= 2:
    print("You are a baby")
elif 2 < age <= 4:
    print("You are a toddler!")
elif 4 < age <= 12:
    print("You are a kid!.")
elif 13 <= age <= 20:
    print("You are a teenager!.")
elif 20 <= age <= 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# py 3.10 alternative - case by case scenario match case

favorite_fruits = ['apple', 'orange', 'pear', 'banana']
if 'apple' in favorite_fruits:
    print("You really like apple!")

if favorite_fruits:
    print("You have favorites in frutis.")

# try it yourself - simple stuff already in above examples
