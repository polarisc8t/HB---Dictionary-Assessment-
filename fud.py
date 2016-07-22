def pairs(numbers):
    i = 0
    my_list = []

    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 0:
	        my_list.append([num1, num2])
	        print [my_list]

numbers = [2,3,5,-2]

pairs(numbers)
