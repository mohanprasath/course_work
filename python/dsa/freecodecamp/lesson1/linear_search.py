def linear(local_data: list, value: int) -> int:
    for number in local_data:
        if number == value:
            return number
    return None


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Is 10 in array:", linear(data, 10))
print("Is 5 in array:", linear(data, 5))

'''
O(n) serach time complexity
'''