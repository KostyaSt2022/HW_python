my_str = '32*x**2 + 4*x - 6 = 0'

new_str = my_str.replace(' ', '').replace('=0', '').replace('*x', '')

print(my_str)
print(new_str)

# new_list = new_str.split('+')
# print(new_list)
# list2 = []
# for i in new_list:
#     list2.append(i.split('*x'))
# print(list2)