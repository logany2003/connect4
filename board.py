

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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pass
    
    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ' ':
                    return False
                else:
                    return True
    
    def disp_board(self):
        print("-" *(2*self.width), end = ' ')
        print()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for row in self.board:
                    for ele in row:
                        print(ele,end=' ')
        print()
            
        print("-" *(2*self.width), end = ' ')
        print()
        
        for i in range(len(self.board)):
            print(i+1, end= ' ')
            
        
          







#
if __name__ == "__main__":
    #test code
    pass
    