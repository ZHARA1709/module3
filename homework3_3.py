def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# part 1
print_params()
print_params(5)
print_params(5, 'false')
print_params('urban',False,5)

print_params(b = 25)
print_params(c = [1, 2, 3])
print('________________________________')

# part 2
values_list = [5, 'five', False]
values_dict = {'a': 6, 'b': 'six', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print('________________________________')

# part 3
values_list_2 = [5.35, 'string']
print_params(*values_list_2, 45)