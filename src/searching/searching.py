debug = False

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if debug: print(arr)
    delta = end - start
    if debug: print(f"delta\t{delta}")
    if delta <= 0:
        return -1
    else:
        mid = (end - start) // 2
        if debug: print(f"target\t{target}   =\tarr[{mid}] ({arr[mid]})\t{arr[mid] == target}")
        if arr[mid] == target:
            if debug: print(f"found {target} at position {mid}")
            return mid
        elif target < arr[mid]:
            if debug: print("lower")
            return binary_search(arr, target, start, mid)
        elif target >= arr[mid]:
            if debug: print("higher")
            return binary_search(arr, target, mid, end)
        else:
            if debug: print("not found")
            return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
