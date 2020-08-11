def sort(numbers):
	for i in range(len(numbers)):
		j = i + 1
		for j in range(len(numbers)):
			if numbers[i] < numbers[j]:
				temp = numbers[i]
				numbers[i] = numbers[j]
				numbers[j] = temp
	return numbers


print(sort([9, 2, 3, 2, 4, 2]))