'''
Input: a List of integers
Returns: a List of integers
'''
# U - we're counting the number of non zero elements in a list and moving those elements to the left of the list.

# P - we can use a counter for the number of elements, and use a method we've previously adopted to move them

# E
def moving_zeroes(arr):
    # we instantiate the counter
    counter = 0
    # and now we rearrange the list
    for i in range(len(arr)):
        if arr[i] != 0: # we don't want to move zeroes
            counter += 1
            arr = [arr[i]] + arr[:i] + arr[i+1:]
    
    return(arr)




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")