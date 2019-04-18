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

def my_for(iterable, func):
    iterator = iter(iterable)
    # print(next(iterator))
    # print(next(iterator))
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print("End of iterator.")
            break
        else:
            func(thing)

my_for("hello", print)
my_for([1,2,3,4], print)