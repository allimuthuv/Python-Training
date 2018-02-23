#!/bin/python
my_list = [1, 'a' , 2.0, 'abc', 5.5, 'last' ]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[::2])
print(my_list[0:])
print(my_list[-1])
print(my_list[1::3])
my_list[4] = 5.0
print(my_list)
my_list.append(False)
print(my_list)
my_list = my_list + ['new1', 'new3']
print(my_list)
my_list[2] = [2, 2.5, 3]
print(my_list)
my_list.remove('abc')
print(my_list)
my_list[2] = []
print(my_list)
my_list.remove('last')
print(my_list)
new_list = [ 1, 2, 3, 5]
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(1)
print(new_list)
