immutable_var = 'yaya', 12, True
print(immutable_var)
#immutable_var[0] = 'yippee' - ошибка, тк элементы кортежа нельзя изменить
mutable_list = ['yaya', 12, True]
mutable_list[0] = 5
mutable_list[1] = 6
print(mutable_list)