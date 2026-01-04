def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1     # fixed: update high, not mid
        else:
            low = mid + 1      # fixed: update low, not mid

    return -1  # not found

# Test it
li = [1, 2, 4, 25, 34, 62]  # sorted!
print(binary_search(li, 2))  # → 1 (correct)
print(binary_search(li, 99)) # → -1 (not found)
