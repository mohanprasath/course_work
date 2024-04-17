class Test:
    def __iter__(self):
        self.count = 1
        return self

    def __next__(self):
        if self.count <= 20:
            self.count += 1
            return self.count
        else:
            raise StopIteration


test = Test()
test_iterator = iter(test)
for i in range(25):
    try:
        print(next(test_iterator))
    except StopIteration:
        print("StopIteration")

