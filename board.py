

class Board:
    def __init__(self, width, height):
        self.board = [[" "]*width for i in range(height)]
        self.width = width
        self.height = height
    
    def add_piece(self, piece, column):
        pass

    def empty_board(self):
        pass
    
    def check_win(self):
        pass
    
    def is_full(self):
        pass
    
    def disp_board(self):
        pass
          







#
#if __name__ == "__main__":
#    #test code
#    b = Board(3,3)
#    b.disp_board()
    