def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [10, False, 3.14]
values_dict = {'a': 6.28, 'b': True, 'c': 12}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [9.42, 'ne true']
print_params(*values_list_2, 42)
