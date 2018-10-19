from board import Board
from player import Player

class Game:
    def __init__(self, board):
        self.turn = 0 #assigns players turn
        self.players = [] #makes player list
        self.board = board #assigns board
    
    def play_game(self): #runs the game
        print("Welcome to connect 4!")
        print("First Player: ")
        self.players.append(Player('x'))
        print("Second Player: ")
        self.players.append(Player('o'))
        
        while True:
            print()
            self.board.disp_board()
            print()
                
            while True:
                try:
                    self.board.add_piece(self.players[self.turn].get_choice(self.board), self.players[self.turn].piece)
                    break
                except Exception as e:
                    print(f'Error {e}')
            if self.board.check_win():
                print(f"{self.players[self.turn]} wins")
                self.board.dispay_board()
                return
            if self.board.is_full():
                print("Draw")
                self.board.display_board()
                return
            self.turn = (self.turn + 1) % 2
            
    
    
    
    
    
    
if __name__ == "__main__":
    # test code
    game = Game(Board(6,7))
    game.play_game()
    # pass