def fav_colors(**kwargs):
    print(kwargs)
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}'")

fav_colors(Richie="Purple", ruby="red", Colt="Purple")