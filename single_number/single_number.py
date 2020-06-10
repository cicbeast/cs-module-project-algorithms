'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# U - there will always be only one number that shows up once. All other numbers repeat once

# P - we can sort the values. This will place the repeats next to eachother.
#     then we can check for repeats using an index loop 

# E
def single_number(arr):
    arr = sorted(arr)
    a = 0
    while a < int(len(arr)/2):
        if arr[(2*a)] != arr[(2*a +1)]:
            return arr[2*a]
        a +=1
    # counter = 0
    # checker = 0

    # for i in arr:
    #     a = 0
    #     checker = i

    #     while a < len(arr):
    #         if arr[a] == checker:
    #             counter += 1
            
    #         a += 1

    #     if counter < 2:
    #         return checker


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")