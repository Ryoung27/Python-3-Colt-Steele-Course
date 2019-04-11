def make_noise():
    print("hello")

make_noise()

def speak_pig():
    return "oink"

speak_pig()

list_even = []
def generate_evens():
    for i in range(1,50):
        if i % 2 == 0:
            list_even.append(i)
    print(list_even)

generate_evens()