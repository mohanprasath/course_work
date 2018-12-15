'''
This is a sample module file to explain the idea of modules.
We are calculating the fibonocii sequence in this module.
'''

def fibonocii(num):
    '''
    This function calculates the fibonocii sequence upto the
    given number num, from 0, 1.
    
    The result is printed on the console. 
    '''
    first, second = 0, 1
    result = []
    result.append(first)
    result.append(second)
    for i in range(num):
        first, second = second, first + second
        result.append(second)
    print(result)

def test_function():
    print("Test function in fibo module")
