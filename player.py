

class Player:
    def __init__(self, piece):
        self.piece = piece
        self.name = self.get_name()
    
    def get_name(self):
        print("what is your name? ")
        name = input("> ")
        return name

    def get_choice(self, Board):
        print(f"{self.name} which column would you like to place your piece in?")
        choice = int(input("> "))
        return choice




if __name__ == "__main__":
    # test code
    # p = Player("red")
    # print(p.choice)
    pass




