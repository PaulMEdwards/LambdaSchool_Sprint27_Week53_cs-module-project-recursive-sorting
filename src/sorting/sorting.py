debug = False

def split(arr):
    m = len(arr) // 2
    return arr[:m], arr[m:]

def merge(arrA, arrB):
    if debug: print("\nBEGIN\tmerge")
    if debug: print(f"arrA\t{arrA}\narrB\t{arrB}")

    la = len(arrA)
    lb = len(arrB)

    if la == 0:
        return arrB
    elif lb == 0:
        return arrA

    ai = bi = 0
    count = la + lb

    sorted = []

    while len(sorted) < count:
        if arrA[ai] <= arrB[bi]:
            sorted.append(arrA[ai])
            ai += 1
        else:
            sorted.append(arrB[bi])
            bi += 1
        if debug: print(f"sorted\n{sorted}")
        if bi == lb:
            sorted += arrA[ai:]
            if debug: print(f"sorted\n{sorted}")
            break
        elif ai == la:
            sorted += arrB[bi:]
            if debug: print(f"sorted\n{sorted}")
            break

    if debug: print("END\tmerge")
    return sorted

def merge_sort(arr):
    if len(arr) > 1:
        LHS, RHS = split(arr)
        if debug: print(f"arr\t{arr}\nLHS\t{LHS}\nRHS\t{RHS}")
        arr = merge(merge_sort(LHS), merge_sort(RHS))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
