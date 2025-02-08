def read_board():
    board = []
    with open("input.txt", "r") as f:
        for row in f.readlines():
            cols = []
            for col in row:
                cols.append(col)

            board.append(cols[:-1])

    return board


if __name__ == "__main__":
    board = read_board()
