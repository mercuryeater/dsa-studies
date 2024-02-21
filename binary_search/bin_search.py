def binary_search(sortedArray, item2find):
    low = 0
    high = len(sortedArray) - 1


    while low <= high:
        mid = (low + high) // 2
        guess = sortedArray[mid]

        # If guess is equal to item the returns the position of the
        # item in the list
        if guess == item2find:
            return mid
        
        if guess < item2find:
            low = mid + 1
        else:
            high = mid - 1
    # If no item is equal to guess returns None
    return None
    
my_list = [1, 3, 5, 7, 9, 10]

print(binary_search(my_list, 7))
print(binary_search(my_list, 8))
