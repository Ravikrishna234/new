def main():
	matrix = []
	for i in range(0,3):
		c=input().split(' ')
		matrix.append(c)
	k = []
	k.append(tictac(matrix))
	if len(k) == 0:
		print('draw')
	if len(k) == 1:
		if k[0] == 'x' or k[0] == 'o':
			print(k[0])
		else:
			print("invalid input")
	else:
		print("invalid game")
def tictac(matrix):
	if matrix[0] == matrix[1] == matrix[2]:
		return matrix[0]
	elif matrix[0][0] == matrix[1][1] == matrix[2][2]:
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
	elif matrix[1][0] == matrix[1][1] == matrix[1][2]:
		return matrix[1][2]
if __name__ == "__main__":
	main()
