# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

my_list = [1, 0, 13, 0, 0, 0, 5]
print(f"start list: {my_list}")
cnt_list = my_list.count(0)
num_list = 1
while num_list <= cnt_list:
    ind_lst = my_list.index(0)
    my_list.append(my_list[ind_lst])
    my_list.pop(ind_lst)
    num_list += 1
print(f"result list: {my_list}")
