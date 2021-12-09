class Tik_tac_toe():
    def __init__(self) -> None:
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.row = int
        self.column = int
        self.current_token = "X"
        self.winner = ""
        self.move_counter = 0

    def make_move(self):
        '''
        Asks player for input of what row and column he wants to place his token in with get_input().
        Checks for error with check_input() if there is an error then asks for new input otherwise places token.
        Raises the move_counter by one and checks if there is an winner.
        '''
        move = self.get_input("normal move")
        error = self.check_input(move)
        while error:
            move = self.get_input(error)
            error = self.check_input(move)
        else:
            self.board[self.row][self.column] = self.current_token
            self.move_counter += 1
            self.check_winner(move)

    def check_input(self, move):
        '''
        Checks if players input is between 1-3 and then checks if the spot is available. 
        . 

        Args:
            move: Players input for his next move. 
                The input needs to be array of 2 strings containing set of "1","2" or "3".

        Returns:
            Returns False if there is no Error otherwise it returns what error it found.
        '''
        legit_moves = [0, 1, 2]
        if len(move) == 2:
            if move[0] in legit_moves and move[1] in legit_moves:
                self.row, self.column = move[0], move[1]
                if self.board[self.row][self.column] == " ":
                    return False
                else:
                    return "spot taken"
            else:
                return "illegal move"
        else:
            return "illegal move"

    def get_input(self, reason):
        '''
        Asks player for his next move. 

        Args:
            reason: The reason for the request. 
                "normal move", "illegal move", "spot taken".

        Returns:
            Returns players input minus 1 as intigers.
        '''
        match reason:
            case "normal move":
                move = (input(
                    f"What row and what column would you like to place your {self.current_token}\n")).split()
            case "illegal move":
                move = (input(
                    f"Please try again. Select row between 1-3 and then column between 1-3 to place your {self.current_token}\n")).split()
            case "spot taken":
                move = (input(
                    f"There is spot is not free please try again.\nSelect row between 1-3 and then column between 1-3 to place your {self.current_token}\n")).split()
        return (int(move[0])-1, int(move[1])-1)

    def swap_token(self):
        '''
        Swaps current token so next player can make a move.
        '''
        if self.current_token == "X":
            self.current_token = "O"
        else:
            self.current_token = "X"

    def print_board(self):
        '''
        Prints out the game board.
        '''
        empty_line = "     |     |   "
        dot_line = "------------------"
        for i in range(len(self.board)):
            print(empty_line)
            print(
                f"  {self.board[i][0]}  |  {self.board[i][1]}  |   {self.board[i][2]}")
            print(empty_line + "")
            if i < 2:
                print(dot_line)

    def check_winner(self, move):
        '''
        Checks if counter is equal or higher then 5 then checks where last move was made.
        Depending on what move was last made it uses diffrent functions to evaluate if the move
        was a winners move or if the game should continue.  

        Args:
            move: Players input for his next move. 
                The input needs to be array of 2 strings containing set of "1","2" or "3".
        '''
        if self.move_counter >= 5:
            middles = ((1, 0), (0, 1), (1, 2), (2, 1))
            corners_left_to_right = ((0, 0), (2, 2))
            corners_right_to_left = ((0, 2), (2, 0))
            center = (1, 1)

            if move in middles:
                self.check_row(move[0])
            elif move in corners_left_to_right:
                self.check_corner_left_to_right()
                self.check_row(move[0])
                self.check_column(move[1])
            elif move in corners_right_to_left:
                self.check_corner_right_to_left()
                self.check_row(move[0])
                self.check_column(move[1])
            elif move == center:
                self.check_row(move[0])
                self.check_column(move[1])
                self.check_corner_left_to_right()
                self.check_corner_right_to_left()
        if self.move_counter == 9:
            self.winner = "draw"

    def check_row(self, row):
        '''
        Checks if there are 3 token in give row. 
        If there is a winner it sets winner to current_token

        Args:
            row: The number of row that needs to be checked.
        '''
        if self.board[row][0] == self.current_token:
            if self.board[row][1] == self.current_token:
                if self.board[row][2] == self.current_token:
                    self.winner = self.current_token

    def check_column(self, column):
        '''
        Checks if there are 3 token in give column. 
        If there is a winner it sets winner to current_token

        Args:
            column: The number of row that needs to be checked.
        '''
        if self.board[0][column] == self.current_token:
            if self.board[1][column] == self.current_token:
                if self.board[2][column] == self.current_token:
                    self.winner = self.current_token

    def check_corner_left_to_right(self):
        '''
        Checks if there is are 3 token in top corner from left to bottum corner right.
        If there is a winner it sets winner to current_token.
        '''
        if self.board[0][0] == self.current_token:
            if self.board[1][1] == self.current_token:
                if self.board[2][2] == self.current_token:
                    self.winner = self.current_token

    def check_corner_right_to_left(self):
        '''
        Checks if there is are 3 token in top corner from right to bottum corner left.
        If there is a winner it sets winner to current_token.
        '''
        if self.board[0][2] == self.current_token:
            if self.board[1][1] == self.current_token:
                if self.board[2][0] == self.current_token:
                    self.winner = self.current_token


def main():
    game = Tik_tac_toe()
    while not game.winner:
        game.print_board()
        game.make_move()
        if not game.winner:
            game.swap_token()
    if game.winner == "draw":
        game.print_board()
        print("There is no winner, it's a draw!")
    else:
        game.print_board()
        print(f"The winner is {game.current_token}!")


if __name__ == "__main__":
    main()
