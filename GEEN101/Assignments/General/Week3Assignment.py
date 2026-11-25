V = [150,200,250,300,400]
a = 340

for v in V:
    M = v / a
    if M < 0.8:
        print(v, "m/s -> Subsonic")
    elif M <= 1.2:
        print(v, "m/s -> Transonic")
    else:
        print(v, "m/s -> Supersonic")
