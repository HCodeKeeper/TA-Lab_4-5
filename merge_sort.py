
def sort(arr):
    if len(arr) == 1:
        return
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]
    sort(left)
    sort(right)

    i=k=j=0
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            arr[j] = left[i]
            i += 1
        else:
            arr[j] = right[k]
            k += 1
        j += 1

    while i < len(left):
        arr[j] = left[i]
        i += 1 
        j += 1
    while k < len(right):
        arr[j] = right[k]
        k += 1
        j += 1

