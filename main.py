from board import board
from exception import FillException

def main():
    player = 0
    Board = board()

    while True:
        if player > 41:
            print("draw")
            return
        Board.display_board()
        print("Player" + str(player % 2 + 1) + " set piece")
        try:
            x = int(input())
            if Board.set_piece(x, player % 2):
                Board.display_board()
                print("Player" + str(player % 2 + 1) + " is winner")
                return
            player += 1
        except ValueError:
            print("Only digit\n")
        except IndexError:
            print("Only between 0 and 6\n")
        except FillException:
            print("Full of pieces\n")

if __name__ == '__main__':
	main()