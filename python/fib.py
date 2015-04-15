def fibs(x):
	result = [0, 1] 
	for index in range(x - 2):
		result.append(result[-2] + result[-1]) 
		return result


if __name__ == '__main__':
	num = input('Enter one number: ') 
	print fibs(num)
