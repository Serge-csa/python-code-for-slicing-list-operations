my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = my_list[2:5]
print(sliced_list)

#negative indices
sliced_list = my_list[-4:-1]
print(sliced_list)

#slicing with a specified step
sliced_list = my_list[1:9:2]
print(sliced_list)

#omitting indices
sliced_list1 = my_list[:5]
print(sliced_list1)
sliced_list2 = my_list[5:]
print(sliced_list2)

#copying a list
copied_list = my_list[:]
print(copied_list)
