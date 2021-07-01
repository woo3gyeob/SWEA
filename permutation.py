for i1 in range(1,5):
    for i2 in range(1,5):
        if i2 != i1:
            for i3 in range(1,5):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)