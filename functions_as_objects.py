def function_a(x, y):
    return x * y

def function_b(x, y):
    return 2 * (x - y)

def overarching_function(x, y, func):
    results_list = []
    results_list.append(func(x, y))
    results_list.append(func((2*x), (2*y)))
    return results_list

print(overarching_function(3, 4, function_b))