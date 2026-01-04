def Binary(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            mid = high - 1
        else:
            mid = low + 1

    return mid

li = [34,25,2,62,4,1]
print(Binary(li,2))
