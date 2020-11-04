# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    aIndex = 0
    bIndex = 0

    for i in range(len(merged_arr)):
        # check if at the end of the a arr
        if aIndex > len(arrA)- 1:
            # since no more elements in a arr add rest of b arr elements
            merged_arr[i] = arrB[bIndex]
            bIndex += 1
        # check if at end of b arr
        elif bIndex > len(arrB) - 1:
            # since no more elements in b arr add rest of a arr elements
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        # not at the end of either array
        else:
            # check which element is smaller and append it to the merged array
            if arrA[aIndex] > arrB[bIndex]:
                merged_arr[i] = arrB[bIndex]
                bIndex += 1
            else:
                merged_arr[i] = arrA[aIndex]
                aIndex += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # find middle value
    middle = len(arr) // 2

    # the left array holds all elements to the left of the middle value
    left = arr[:middle]

    # right array holds all elements to the right of that
    right = arr[middle:]

    # if there's more than 1 number in the left array
    # checks for base case on left array
    if len(left) > 1:
        left = merge_sort(left)

    # if there's more than 1 number in the right array
    # checks for base case on right array
    if len(right) > 1:
        right = merge_sort(right)

    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

