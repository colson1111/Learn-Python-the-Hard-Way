def while_loop_ex(j):
	i = 0
	numbers = []

	while i < j:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
		
		
while_loop_ex(10)
