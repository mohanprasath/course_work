# dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_coordinate'] = 0
alien_0['y_coordinate'] = 25
print(alien_0)

# keys in dictionary are usually in the order of entry
print(alien_0.keys())

alien_1 = {'color': 'red', 'points': 3, 'x_coordinate': 14, 'y_coordinate': 16}
print(alien_1)
print(alien_1.keys())
del alien_1['x_coordinate']
del alien_1['y_coordinate']
print(alien_1)
print(alien_1.get('x_coordinate', "x_coordinate value doesn't exist"))

# try it yourself
person = {'first_name': 'John', 'age': 20, 'city': 'New York', 'favorite_color': 'green', 'last_name': 'Walker'}
print(person)
for key, value in person.items():
    print(f'Key: {key}')
    print(f'value: {value}')

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ['phil', 'sarah', 'edward', 'jacob']
for friend in friends:
    print(f"Hello {friend.title()}")

    if friend in favorite_languages:
        print(f"\t{friend.title()}'s favorite language is {favorite_languages[friend]}")
    else:
        print(f"\t{friend.title()}, can you take our favorite programming language poll!")

