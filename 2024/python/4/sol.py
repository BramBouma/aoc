class Solution:
    def __init__(self, word: str):
        self.word = word
        self.board = self._read_input()
        self.init_locs = self._find_initial()
        # self.target_locs = self._find_target()

    def _read_input(self):
        input_lines = []
        with open("input.txt", "r") as f:
            for row in f.readlines():
                cols = []
                for col in row:
                    cols.append(col)

                input_lines.append(cols[:-1])

        return input_lines

    def _find_initial(self):
        init_list = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == self.word[0]:
                    # print(i, j)
                    init_list.append([i, j])
                else:
                    continue

        return init_list

    def _find_target(self, targ: str | int):
        if type(targ) is str and targ not in self.word:
            raise IndexError("no target in word")
        else:
            pass

        targ_list = []
        match targ:
            case str():
                for i in range(len(self.board)):
                    for j in range(len(self.board[0])):
                        if self.board[i][j] == targ:
                            targ_list.append([i, j])

            case int():
                for i in range(len(self.board)):
                    for j in range(len(self.board[0])):
                        if self.board[i][j] == self.word[targ]:
                            targ_list.append([i, j])

        return targ_list

    def _search_dir(self, loc: list[int], dir: list[int]):
        for i in range(len(self.word) - 1):
            shift = [x * (i + 1) for x in dir]
            loc_shift = [sum(x) for x in zip(loc, shift)]

            # comment out first two if statements and change third
            # from 'elif' to 'if' if want to use 'try except IndexError'
            if not 0 <= loc_shift[0] < len(self.board):
                return False

            elif not 0 <= loc_shift[1] < len(self.board[0]):
                return False

            # comment until above comment lines and change below
            elif self.board[loc_shift[0]][loc_shift[1]] != self.word[i + 1]:
                return False

            else:
                continue

        return True

    def _search_loc(self, loc: list[int]):
        dirs = [
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
        ]
        n_loc_words = 0

        for dir in dirs:
            if self._search_dir(loc, dir):
                n_loc_words += 1

            else:
                continue

        return n_loc_words

    def count_total_matches(self):
        loc_matches = []
        for loc in self.init_locs:
            loc_matches.append(self._search_loc(loc))

        return sum(loc_matches)


if __name__ == "__main__":
    board = Solution("XMAS")

    # print(board.board)
    print("Board rows: ", len(board.board))
    print("Board cols: ", len(board.board[0]))
    print("Number of Xs: ", len(board.init_locs))

    sol_first = board.count_total_matches()
    print("Part 1: ", sol_first)

    print("Number of As: ", len(board._find_target("A")))
