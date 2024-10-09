wave = int(input())

if 620 <= wave <= 780:
    print("Red")
elif 590 <= wave < 620:
    print("Orange")
elif 570 <= wave < 590:
    print("Yellow")
elif 495 <= wave < 570:
    print("Green")
elif 450 <= wave < 495:
    print("Blue")
elif 425 <= wave < 450:
    print("Indigo")
else:
    print("Violet")