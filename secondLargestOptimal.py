def optimal(arr):
    largest = secondLargest = float("-inf")


    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and secondLargest!= largest:
            secondLargest = num

    if secondLargest != float("-inf"):
        return secondLargest


    return "Not Found"


arr = [3, 5, 1, 2, 4, 8, 7]
print("second largest: ", optimal(arr))