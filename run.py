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
        """
        Random displacement of carrots on board.
        Give the carrot the mark of "X".
        """
        for carrot in range(5):
            carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            while self.board[carrot_r][carrot_cl] == "X":
                carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            self.board[carrot_r][carrot_cl] = "X"
    
    def get_user_input(self):
        """
        The users input to game and response to inputs.
        """
        try:
            row = input("Look for carrot on row(1-5)...: ")
            while row not in '12345':
                print('Not valid! Select a valid row(1-5).')
                row = input("Look for carrot on row(1-5)...: ")
            column = input("Choose a column(A-E): ").upper()
             while column not in "ABCDE":
                print('Not valid! Select a valid column(A-E).')
                column = input("Choose a column(A-E): ").upper()
            return int(row) - 1, \
                Board.letters_to_numbers(self)[column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()
    
    def find_carrots(self):
        """
        Tells what happens on the board when finding carrot.
        """
         find_carrots = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    find_carrots += 1
        return find_carrots


def GameOver():


def Play_Game():
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_guess_board = Board([[" "] * 5 for i in range(5)])
    Carrots.create_carrots(computer_board)
    turns = 5
     while turns > 0:
        Board.print_board(user_guess_board)
        # get user input
        user_x_row, user_y_column = Carrots.get_user_input(object)
        # check if duplicate guess