# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes

# class Vechicle:
#     pass

# car = Vechicle()
# boat = Vechile()

# class User:
#     pass

# user1 = User()

# def add:
#     return 3

# deck = Deck()
# deck.shuffle()
# hand1 = deck.deal_hand(5)
# hand2 = deck.deal_hand(5)
# print(hand1)
# print(hand2)
# deck.reset()

class User:
    def __init__(self, first, last, age):
        # print("A new user has been made.")
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} is {self.age}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "", 30)
user3 = User("Red", "Forman", 55)

print(user2.first, user2.last)
print(user2)