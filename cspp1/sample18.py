"""SAMPLE"""
def normalize(numbers):
	"""samp"""
	max_number = max(numbers)
	for i in range(len(numbers)):
		numbers[i] /= float(max_number)
	return numbers
def main():
	"""samp"""
	try:
		normalize([0,0,0])
	except ZeroDivisionError:
		print("Invalid Maximum element")
if __name__ == "__main__":
	main()
