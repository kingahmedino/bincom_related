def fibonacci(seq):
	fib_list = [0, 1]
	for i in range(seq - 2):
		fib_len = len(fib_list)
		fib_list.append(fib_list[fib_len - 2] + fib_list[fib_len - 1])
	print(fib_list)