class Test:
    def __iter__(self):
        self.count = 1
        return self

    def __next__(self):
        self.count += 1
        return self.count


test = Test()
test_iterator = iter(test)
print(next(test_iterator))
print(next(test_iterator))
print(next(test_iterator))
print(next(test_iterator))
