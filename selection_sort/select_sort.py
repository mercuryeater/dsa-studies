def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        # If we wanted to sort by biggest
        # we would only have to change the
        # comparison sign from < to >
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        
    return smallest_index

def selection_sort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # We take out the smallest item 
        # and put it in the other list
        newArr.append(arr.pop(smallest))
    
    return newArr
        

print(selection_sort([5, 3, 6, 2, 10]))