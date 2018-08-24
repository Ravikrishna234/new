def main():
	matrix = []
	for i in range(0,3):
		c=input().split(' ')
		matrix.append(c)
	print(tictac(matrix))
def tictac(matrix):
	player_= []
	for i in matrix:
		if i[0] == i[1] == i[2]:
			player_.append(i[0])
	for i in range(0,3):
		if matrix[0][i] == matrix[1][i] == matrix[2][i]:
			player_.append(matrix[0][i])
	if matrix[0][0] == matrix[1][1] == matrix[2][2]:
		player_.append(matrix[1][1])
	elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
		player_.append(matrix[1][1])
	if len(player_) == 0:
		print('draw')
		if player_[0] == 'x' or player_[1] == 'o':
			print(player_[0])
		else:
			print("invalid input")
		return player_[0]
	else:
		print("invalid game")
	return None
if __name__ == "__main__":
	main()
