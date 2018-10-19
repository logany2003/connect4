from board import Board
from player import Player

class Game:
    def __init__(self, board):
        self.turn = 0 #assigns players turn
        self.players = [] #makes player list
        self.board = board #assigns board
    
    def play_game(self):
        '''runs the game of connect 4'''
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
                self.board.disp_board()
                print(f"{self.players[self.turn].name} wins")
                return
            if self.board.is_full():
                self.board.disp_board()
                print("Draw")
                return
            self.turn = (self.turn + 1) % 2
            
    
    
    
    
    
    
if __name__ == "__main__":
    # test code
    game = Game(Board(6,7))
    game.play_game()
    # pass