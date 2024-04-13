import this

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)
print("\t python")
print("Languages:\n\tPython\n\tC\n\tC++\n\tJavaScript")

fav_lang = " Python "
print(fav_lang)
print(fav_lang.upper())
print(fav_lang.lower())
print(fav_lang.title())
print(fav_lang)
print(fav_lang.strip())
print(fav_lang.rstrip())
print(fav_lang.lstrip())

nostarch_url = 'https://www.nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))

try:
    mesage = 'One of Python\'s strengths is its diverse community.'
    print(mesage)
except Exception as e:
    print(e)

print("Done")

# underscores in numbers
universe_age = 14_000_000_000
print(universe_age)

x, y, z = 0, 0, 0
MAX_CONNECTIONS = 5000

print(5+3)
print(5-3)
print(5*3)
print(5/3)

value = 10
print(value)