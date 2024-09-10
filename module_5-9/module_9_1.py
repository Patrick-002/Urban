def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        new_list = function(int_list)
        results[function.__name__] = new_list
    return results

if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))