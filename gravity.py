def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [55,7,78,12,42]
print(bubblesort(arr))