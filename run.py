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
        print("  A B C D E")
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
        for i in range(5):
            carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            while self.board[carrot_r][carrot_cl] == "X":
                carrot_r, carrot_cl = randint(0, 4), randint(0, 4)
            self.board[carrot_r][carrot_cl] = "X"

    def get_user_input(self):
        """
        Get users inputs in the game and responding.
        """
        try:
            row = input("Look for carrot on row(1-5)...: ")
            if row not in '12345':
                print("Not valid! Select a valid row(1-5).")
                row = input("Look for carrot on row(1-5)...: ")
            column = input("Choose a column(A-E): ").upper()
            if column not in "ABCDE":
                print("Not valid! Select a valid column(A-E).")
                column = input("Choose a column(A-E): ").upper()
            return int(row) - 1, \
                Board.letters_to_numbers(self)[column]
        except (ValueError, KeyError):
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


def game_over():
    """
    End game or loose
    """
    user_input = input("Play again (Y/N)? ").upper()
    if user_input == "Y":
        play_game()
    if user_input == "N":
        print("Thank you for playing!")
        exit()


def play_game():
    """
    Creating board, duplicate answer,found a carrot/not found,
    win/loose game, turns, game over.
    """
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_guess_board = Board([[" "] * 5 for i in range(5)])
    Carrots.create_carrots(computer_board)
    turns = 5
    while turns > 0:
        Board.print_board(user_guess_board)
        user_x_row, user_y_column = Carrots.get_user_input(object)
        if user_guess_board.board[user_x_row][user_y_column] == "-"\
                or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You searched there already")
            user_x_row, user_y_column = Carrots.get_user_input(object)

        if computer_board.board[user_x_row][user_y_column] == "X":
            print("YEAH! You found a carrot!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("Sorry! No carrot!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
            
        if Carrots.find_carrots(user_guess_board) == 5:
            print("CONGRATULATION! You found all 5 carrots! Yum! carrotcake!")
            game_over()
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Game Over")
                game_over()


if __name__ == "__main__":
    play_game()