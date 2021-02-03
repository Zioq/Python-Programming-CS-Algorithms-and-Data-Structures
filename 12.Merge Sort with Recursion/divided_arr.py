# Recursive divide function

def divide_arr(arr):
    # Base case
    if len(arr)< 2:
        print(f"Base condition reached with {arr[:]}")
        # return all value in the list
        return arr[:]
    else:
        # integer division
        middle = len(arr)//2
        print("Current list to work with:", arr)
        print("Left split: ", arr[:middle])
        print("Right split: ", arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        print(l1, l2)
        # implied return None
l = [8,6,2,5]
divide_arr(l)