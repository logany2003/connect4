

class Board:
    def __init__(self, width, height):
        self.board = [[" "]*width for i in range(height)]
        self.width = width
        self.height = height
    
    def add_piece(self, piece, column):
        for row in range(self.height-1 , -1, -1):
            if self.board[row][column-1] == ' ':
                self.board[row][column-1] = piece
                break
        else:
            raise ValueError("invalid")

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
        print("-" *(2*self.width-1), end = ' ')
        print()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j],end=' ')
            print()
            
        print("-" *(2*self.width-1), end = ' ')
        print()
        
        for i in range(len(self.board)):
            if i < self.width:
                print(i+1, end= ' ')
            
        
          
def main():
     b = Board(6,7)
     b.add_piece("y", 2)
     b.disp_board()





#
if __name__ == "__main__":
    main()

    