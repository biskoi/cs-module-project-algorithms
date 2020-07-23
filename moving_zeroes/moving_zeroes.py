'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    result = []

    for i in arr:
        if i == 0:
            result.append(i)
        else:
            result.insert(0, i)

    return result
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(moving_zeroes([0, 1, 4, 6, 0, 4, 0, 3, 5]))