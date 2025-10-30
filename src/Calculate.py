import numpy as np
import statistics as st

TRUE = 'true yes 1'


def get_data():
    string_data = input(
        "Please input numbers for the selected operation separated by commas (1,2,3) ")
    data = [int(num.strip()) for num in string_data.split(',')]
    return data


def mean(nums):
    average = 0
    for num in nums:
        average += num
    return average / len(nums)


def variance(nums):
    return np.var(nums)


def standard_deviation(nums):
    return st.stdev(nums)


def solve_linear_eq(data):
    # 5x+10 = 35, 8x-10 = 30
    a = np.array([8, -10])
    b = np.array([30])
    return np.linalg.solve(a, b)


def keep_calculating():
    keep_calc = input('Would you like to do another calculation (yes, no, true, false) ')
    if keep_calc.strip().lower() in TRUE:
        return True
    else:
        return False
