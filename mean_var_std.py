import numpy as np

input_list = eval(input('Enter a list of 9 numbers: '))
def calculate(arr):
    
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers")

    matrix = np.array(arr).reshape(3, 3)

    result = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    }

    return result

result_dict = calculate(input_list)

print(result_dict)
