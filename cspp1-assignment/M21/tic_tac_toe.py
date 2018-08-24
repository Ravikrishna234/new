"""TICTACTOE"""
def tic_tac(matrix):
    """tictac"""
    player_ = []
    for i in matrix:
        if i[0] == i[1] == i[2]:
            player_.append(i[0])
    for i in range(0, 3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            player_.append(matrix[0][i])
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        player_.append(matrix[1][1])
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        player_.append(matrix[1][1])
    if player_ == []:
        print("draw")
        return None
    if len(player_) == 1:
        if player_[0] == 'x' or player_[0] == 'o':
            print(player_[0])
        else:
            print("invalid input")
            return player_[0]
    else:
        print("invalid game")
        return None
def main():
    """tictac"""
    matrix = []
    for _ in range(0, 3):
        list_ = input().split(' ')
        matrix.append(list_)
    tic_tac(matrix)
if __name__ == "__main__":
    main()
