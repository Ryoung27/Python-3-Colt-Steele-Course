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

def yell(scream_it):
    return scream_it.upper()

print(yell("ahhhh"))

def speak(animal):
    if animal == "pig":
        return "Oink"
    elif animal == "duck":
        return "Quack"
    elif animal == "cat":
        return "Meow"
    elif animal == None:
        animal == "dog"
    elif animal == "dog":
        return "Bark"
    else:
        return "???"

print(speak("dog"))
print(speak("cat"))
print(speak("dog"))
print(speak("m"))

