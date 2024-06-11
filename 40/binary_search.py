def binary_search(sequence, target):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < target:
            low = mid + 1
        elif sequence[mid] > target:
            high = mid - 1
        else:
            return mid
    return None
