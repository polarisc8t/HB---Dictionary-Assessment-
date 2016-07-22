def foo(numbers):
    i = 0
    my_list = []

    for num1 in numbers:
        for num2 in numbers:
	    if num1 + num2 == 0:
 	        my_list.append([num1, num2])
		print num1, num2    
    return my_list 

numbers = [5,-1,3,-5]
foo(numbers)



