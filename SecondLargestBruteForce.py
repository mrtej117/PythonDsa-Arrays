# input 

# arr = [ 1 ,4 ,7, 8 ,9 ,4,2 ,0]


def brute_force(arr):

    secondlargest = sorted(arr ,reverse = True)

    return secondlargest[1]


arr = [ 1 ,4 ,7, 8 ,9 ,4,2 ,0]
print("Second Largest :" ,brute_force(arr))
