def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params("string", False, 5)
print_params(1, 2)
# print_params(1, 1, 1, 1, 1, 1) print_params() takes from 0 to 3 positional arguments but 6 were given
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, False, (1, 2, 3)]
values_dict = {"a":1, "b":2, "c":3}
print_params(*values_list)
print_params(**values_dict)

values_dict_2 = ["apple", 3.26]
print_params(*values_dict_2, 42)
