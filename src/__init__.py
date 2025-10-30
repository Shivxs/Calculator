# Build a command-line calculator that supports:
# user input
#     match
# Basic arithmetic
# Mean, variance, standard deviation
#
# Bonus: Linear equation solver (ax + b = 0)
#
# Skills: Python basics, functions, error handling, numpy.
#
# Portfolio value: Shows you can handle code fundamentals and math essentials.
import Calculate

basic_arithmetic = '1 basic arithmetic ba'
mean_sd_variance = '2 mean variance standard deviation'
linear_equation = '3 linear equations'
mean = '1 mean m'
variance = '2 variance v'
standard_deviation = '3 standard deviation sd'
all_operations = '4 all a'
keep_calculating = True

print("Hello I'm a Calculator")
while keep_calculating:
    operation = input("""Would you like to do
                  1: Basic Arithmetic
                  2: Calculate the Mean, Variance, or Standard Deviation
                  3: Solve Linear Equations
                  """)
    match operation:
        case operation if operation.lower() in basic_arithmetic:
            to_calc = input('Please type in what you would like to do ')
            print('Result: ' + str((eval(to_calc))))
        case operation if operation.lower() in mean_sd_variance:
            sub_operation = input("""Please input what operation you would like done 
            1) Mean, 2) Variance, 3) Standard Deviation, or 4) All """)
            match sub_operation:
                case sub_operation if sub_operation.lower() in mean:
                    data = Calculate.get_data()
                    print('Mean: ' + str(Calculate.mean(data)))
                case sub_operation if sub_operation.lower() in variance:
                    data = Calculate.get_data()
                    print('Variance: ' + str(Calculate.variance(data)))
                case sub_operation if sub_operation.lower() in standard_deviation:
                    data = Calculate.get_data()
                    print('Standard Deviation: ' + str(Calculate.standard_deviation(data)))
                case sub_operation if sub_operation.lower() in all_operations:
                    data = Calculate.get_data()
                    print('Mean: ' + str(Calculate.mean(data)))
                    print('Variance: ' + str(Calculate.variance(data)))
                    print('Standard Deviation: ' + str(Calculate.standard_deviation(data)))
        case operation if operation.lower() in linear_equation:
            data = input("""Please input your equations in the following format ax+b = # separated by commas
            5x+10 = 35, 8x-10 = 30""")
            print('Value of X : ' + str(Calculate.solve_linear_eq(data)[0]))
        case _:
            print('no matching operation')
            keep_calculating = Calculate.keep_calculating()
    keep_calculating = Calculate.keep_calculating()

