#!/usr/bin/python3
def max_integer(my_list=[]):
max=my_list[0]
for i in my_list:
	if i >= max :
		return(i)
	else:
		return(max)
