from random import randint


class Board:
    def __init__(self, board):
        self.board = board

    def letters_to_numbers(self):
        """
        Transform letters to numbers to our boardgame column.
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        """
        Printing letters to the board.
        Adding numbers as rows in our boardgame.
        Creating and defying the inputs on the board.
        Make our board start with number 1.
        """
        print('  A B C D E')
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Carrots:
    def __init__(self, board):
        self.board = board

    def create_carrots(self):
        for carrot in range(5):
            carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            while self.board[carrot_r][carrot_cl] == 'X':
                carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            self.board[carrot_r][carrot_cl] = 'X'