# name = "Oprah"
# next(name)

# it = iter(name)
# next(it)

#Custom for loop
# for num in [1,2,3]
# for char in "hi there"

# iter()
# next()
# next()

# def my_for(iterable, func):
#     iterator = iter(iterable)
#     # print(next(iterator))
#     # print(next(iterator))
#     while True:
#         try:
#             thing = next(iterator)
#         except StopIteration:
#             print("End of iterator.")
#             break
#         else:
#             func(thing)

# my_for("hello", print)
# my_for([1,2,3,4], print)

class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num



c = Counter(0, 10)
iter(c)

for x in Counter(0,4):
    print(x)