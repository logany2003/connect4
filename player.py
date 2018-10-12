

class Player:
    def __init__(self, piece, name):
        self.piece = piece
        self.name = name
    
    def get_name(self):
        print("what is your name? ")
        name = input(": ")
        return name

    def get_choice(self, Board):
        print("Which column would you like to place your piece in?")
        choice =input(": ")
        return choice




if __name__ == "__main__":
    # test code
    # p = Player("red","AG")
    # print(p.name)
    pass





