from exception import FillException

class board:

    def __init__(self):
        self.Board = [[" " for j in range(7)] for i in range(6)]

    def display_board(self):
        print()
        print(" 0 1 2 3 4 5 6 ")
        print("+-+-+-+-+-+-+-+")
        for oneline in self.Board:
            print("|", end="")
            for piece in oneline:
                print(piece, end="|")
            print("\n+-+-+-+-+-+-+-+")
        print("Player1 = O")
        print("Player2 = X")
        print()

    def set_piece(self, row, player):
        if (row < 0 or 6 < row):
            raise IndexError
        for col_re in range(7):
            col = 5 - col_re
            if col < 0:
                raise FillException()
            if self.Board[col][row] == " ":
                if player == 1:
                    self.Board[col][row] = "X"
                else:
                    self.Board[col][row] = "O"
                break
        return self.is_clear((col), row)

    def is_clear(self, col, row):
        check_list = [
            [[0, -1], [0, 1]],
            [[1, 0], [-1, 0]],
            [[-1, -1], [1, 1]],
            [[1, -1], [-1, 1]],
        ]
        return self.check_all(check_list, col, row)

    def check(self, col, row, colflag, rowflag, linenum):
        for index in range(7):
            coladd = colflag * index
            rowadd = rowflag * index
            if self.is_in_board(col + coladd, row + rowadd) == False:
                break
            if self.is_in_board(col + coladd, row + rowadd) and self.Board[col + coladd][row + rowadd] == self.Board[col][row]:
                linenum += 1
            else:
                break
        return linenum

    def is_in_board(self, col, row):
        return 0 <= col and col <= 5 and 0 <= row and row <= 6

    def check_all(self, list, col, row):
        for checkline in list:
            linenum = -1
            for checkdir in checkline:
                linenum = self.check(col, row, checkdir[0], checkdir[1], linenum)
            if linenum > 3:
                return True
        return False
