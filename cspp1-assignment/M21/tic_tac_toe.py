def main():
	matrix = []
	for i in range(0,3):
		matrix.append(input().split(' '))
	print(tictac(matrix))
def tictac(matrix):
	if matrix[0][0] == matrix[1][1] == matrix[2][2]:
		return matrix[0][0]
	elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
		return matrix[0][2]
	elif matrix[0][0] == matrix[0][1] == matrix[0][2]:
		return matrix[0][0]
	elif matrix[2][0] == matrix[2][1] == matrix[2][2]:
		return matrix[2][2]
	elif matrix[0][0] == matrix[1][0] == matrix[2][0]:
		return matrix[0][0]
	elif matrix[0][2] == matrix[1][2] == matrix[2][2]:
		return matrix[2][2]
	elif matrix[0][1] == matrix[1][1] == matrix[2][1]:
		return matrix[2][1]
if __name__ == "__main__":
	main()
