class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        return ['FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 ==0  else str(num) for num in range(1, n+1)]
