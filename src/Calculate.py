import numpy as np
import statistics as st
import re

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
    pattern = '[+-]*[0-9]*[a-zA-Z]'
    coefficients = []
    products = []
    equations = data.split(',')
    for eq in equations:
        pieces = eq.split('=')
        coefficients_raw = re.findall(pattern,pieces[0])
        for co in coefficients_raw:
            co = co[:-1].strip()
            if not co or co is '+':
                coefficients.append('1')
            elif co is '-':
                coefficients.append('-1')
            else:
                coefficients.append(co)
        products.append(pieces[1].strip())
    return np.linalg.solve(np.array(coefficients).reshape(2,2).astype(int), np.array(products).astype(int))


def keep_calculating():
    keep_calc = input('Would you like to do another calculation (yes, no, true, false) ')
    if keep_calc.strip().lower() in TRUE:
        return True
    else:
        return False
