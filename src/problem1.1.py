import numpy as np

def border_with_zeros(arr):
    '''
    Takes in a 2D numpy array and adds
    a border of zeros around the outer edge

    Example:

        arr = np.array([
            [1,1],
            [1,1]
        ])
        border_with_zeros(arr)

    Would return:

        np.array([
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ])
    '''
    # your code here!

    z_matrix = np.zeros((arr.shape[0] + 2, arr.shape[1] + 2))
    z_matrix[1:-1, 1:-1] = arr
    return z_matrix

if __name__ == '__main__':
    # Test your code here!
    arr = np.array([
        [1,1],
        [1,1]
    ])
    print(border_with_zeros(arr))

