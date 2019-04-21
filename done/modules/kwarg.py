def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}'")

fav_colors(Richie="Purple", ruby="red", Colt="Purple")

# def combine_words(**kwargs):
#     for i, prefix in kwargs.items():
#         print(f"{i}{prefix}")

# combine_words("child", prefix="ish")

def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word