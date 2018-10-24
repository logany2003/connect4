

class Board:
    def __init__(self, width, height):
        self.board = [[" "]*width for i in range(height)]
        self.width = width
        self.height = height
    
    def add_piece(self, column, piece):
        ''' Adds a piece to specified column in the board
        '''
        for row in range(self.height-1 , -1, -1):
            if column <= 0 or column > self.width: # column 0 should raise an error
                raise ValueError("Invalid Column")
            if self.board[row][column-1] == " ":
                self.board[row][column-1] = piece
                break
        else:
            raise ValueError("Column Full")
            

    def empty_board(self):
        ''' Empties board by replacing all columns with " "
        '''
        self.board = [[" "]*self.width for i in range(self.height)]
    
    def check_win(self):
        ''' checks for 4 similar pieces in a row vertically, horizontally, and diagonally
        '''
        for i in range(self.height):
            for j in range(self.width-3):   #Horizontal Check
                if self.board[i][j] != " ":
                    hcheck = [self.board[i][j] , self.board[i][j+1], self.board[i][j+2], self.board[i][j+3]]
                    for c in range(len(hcheck)):
                        if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                            return True
                        
        for i in range(self.height-3):
            for j in range (self.width-3):
                if self.board[i][j] != " ":
                    vcheck = [self.board[i][j] , self.board[i+1][j], self.board[i+2][j], self.board[i+3][j]]
                    for c in range(len(vcheck)):
                        if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] ==  self.board[i+3][j]:
                            return True
                    
        for i in range(self.height-3):      # major Diag Check
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    mdcheck = [self.board[i][j] , self.board[i+1][j+1], self.board[i+2][j+2], self.board[i+3][j+3]]
                    for c in range(len(mdcheck)):
                        if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] ==  self.board[i+3][j+3]:
                            return True
        
        for i in range(3,self.height):      # minor Diag Check
            for j in range(self.width-3):
                if self.board[i][j] != " ":
                    midcheck = [self.board[i][j] , self.board[i-1][j+1], self.board[i-2][j+2], self.board[i-3][j+3]]
                    for c in range(len(midcheck)):
                        if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] ==  self.board[i-3][j+3]:
                            return True
            
            
                    
        
        
        return False
                
                
               
                
    
    def is_full(self):
        ''' Determines if board is full, based on space left in columns
        '''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ' ':
                    return False
        else:
            return True
    
    def disp_board(self):
        ''' displays current board
        '''
        print("-" *(2*self.width), end = ' ')
        print()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j],end=' ')
            print()
            
        print("-" *(2*self.width), end = ' ')
        print()
        
        for row in range(len(self.board[i])):
            print(row+1, end= ' ')
            
    # does not print a newline at the end
          
def main():
    
     b = Board(7,6)
     b.add_piece(1, "4")
     b.add_piece(1, "4")
     b.add_piece(1, "4")
     b.add_piece(1, "4")
     b.add_piece(2, "4")
     b.add_piece(3, "0")
     b.add_piece(4, "0")
     b.add_piece(5, "0")
     b.add_piece(5, "0")
     b.add_piece(2, "4")
     b.add_piece(4, "0")
     b.add_piece(4, "0")
     b.add_piece(3, "0")
     b.add_piece(3, "0")
     b.add_piece(4, "4")
     
  
  
     
     
     
     
     
     
     b.disp_board()
     b.disp_board()
     b.check_win()
     print(b.check_win())

#


#
if __name__ == "__main__":
    main()

#    