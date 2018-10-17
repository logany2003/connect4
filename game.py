from board import Board
from player import Player

class Game:
    def __init__(self, board):
        self.turn = 0
        self.players = []
        self.board = board
    
    def play_game(self):
        print("Welcome to connect 4!")
        print("First Player: ")
        self.players.append(Player('x'))
        print("Second Player: ")
        self.players.append(Player('o'))
        
        while True:
            print()
            self.board.disp_board()
            print()
            try:
                print()
                self.board.add_piece(self.players[self.turn].piece, self.players[self.turn].get_choice(self.board))
                if self.board.check_win():
                    print(f"{self.players[self.turn]} wins")
                    self.board.dispay_board()
                    return
                if self.board.is_full():
                    print("Draw")
                    self.board.display_board()
                    return
                self.turn = (self.turn + 1) % 2
            except Exception as e:
                print(f'Error {e}')
    
    
    
    
    
    
if __name__ == "__main__":
    # test code
    # game = Game(Board(6,7))
    # game.play_game()
    pass