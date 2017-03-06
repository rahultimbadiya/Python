import os


class Player:
    """represents a players of game and results"""

    def __init__(self):
        """Constructor that initialze the values"""
        self.won = 0
        self.lost = 0
        self.draw = 0
        self.name = ''
        self.symbol = ''

    def get_score(self):
        """return the score of player"""
        return (self.won*2)+self.draw-self.lost

    def __str__(self):
        """print the player name,symbol and his score"""
        return '(Player:'+self.name+',Mark:'+self.symbol+',Score:'+str(self.get_score())+')'

    def __lt__(self, other):
        """compare the players score"""
        return self.get_score() < other.get_score()


class Deck:
    """represents a board of game and player choices """

    decklist = ['1','2','3','4','5','6','7','8','9']
    player1_choices = []
    player2_choices = []

    def __init__(self):
        pass

    def __str__(self):
        """print the places selected by the players"""
        return ''+str(self.decklist[0])+'   |'+str(self.decklist[1])+'   |'+str(self.decklist[2])+'\n-----------\n'+str(self.decklist[3])+'   |'+str(self.decklist[4])+'   |'+str(self.decklist[5])+'\n-----------\n'+str(self.decklist[6])+'   |'+str(self.decklist[7])+'   |'+str(self.decklist[8])+''


class Tictactoe():
    """represents a main logic of program """
    print("Welcome to Tic tac toe game")
    p1 = Player()
    p2 = Player()
    p1.name = input("Enter player1 name:")
    p1.symbol = input("Enter player1 symbol:")
    p2.name = input("Enter player2 name:")
    p2.symbol = input("Enter player2 symbol:")

    def is_win(self):
        """check the winning position enter by player"""

        if((d1.decklist[7-1] == d1.decklist[9-1] and d1.decklist[8-1] == d1.decklist[9-1]) or
                 (d1.decklist[4-1] == d1.decklist[6-1] and d1.decklist[5-1] == d1.decklist[6-1])or
                 (d1.decklist[1-1] == d1.decklist[3-1] and d1.decklist[2-1] == d1.decklist[3-1])or
                 (d1.decklist[7-1] == d1.decklist[1-1] and d1.decklist[4-1] == d1.decklist[1-1])or
                 (d1.decklist[3-1] == d1.decklist[9-1] and d1.decklist[6-1] == d1.decklist[9-1])or
                 (d1.decklist[8-1] == d1.decklist[2-1] and d1.decklist[5-1] == d1.decklist[2-1])or
                 (d1.decklist[7-1] == d1.decklist[3-1] and d1.decklist[5-1] == d1.decklist[3-1])or
                 (d1.decklist[9-1] == d1.decklist[1-1] and d1.decklist[5-1] == d1.decklist[1-1])):

             if((d1.decklist[7-1] == self.p1.symbol and d1.decklist[9-1]== self.p1.symbol and d1.decklist[8-1] == self.p1.symbol)or
                (d1.decklist[4-1] == self.p1.symbol and d1.decklist[6-1]== self.p1.symbol and d1.decklist[5-1] == self.p1.symbol)or
                 (d1.decklist[1-1] == self.p1.symbol and d1.decklist[3-1]== self.p1.symbol and d1.decklist[2-1] == self.p1.symbol)or
                 (d1.decklist[7-1] == self.p1.symbol and d1.decklist[1-1]== self.p1.symbol and d1.decklist[4-1] == self.p1.symbol)or
                 (d1.decklist[3-1] == self.p1.symbol and d1.decklist[9-1]== self.p1.symbol and d1.decklist[6-1] == self.p1.symbol)or
                 (d1.decklist[8-1] == self.p1.symbol and d1.decklist[2-1]== self.p1.symbol and d1.decklist[5-1] == self.p1.symbol)or
                 (d1.decklist[9-1] == self.p1.symbol and d1.decklist[1-1]== self.p1.symbol and d1.decklist[5-1] == self.p1.symbol)or
                 (d1.decklist[7-1] == self.p1.symbol and d1.decklist[3-1]== self.p1.symbol and d1.decklist[5-1] == self.p1.symbol)):
                 self.p1.won = self.p1.won +1
                 self.p2.lost = self.p2.lost -1
                 return self.p1.symbol
             else:

                 self.p2.won = self.p2.won +1
                 self.p1.lost = self.p1.lost -1
                 return self.p2.symbol

        elif((d1.decklist[0]==self.p1.symbol or d1.decklist[0]==self.p2.symbol)and
                (d1.decklist[1]==self.p1.symbol or d1.decklist[1]==self.p2.symbol)and
                (d1.decklist[2]==self.p1.symbol or d1.decklist[2]==self.p2.symbol)and
                (d1.decklist[3]==self.p1.symbol or d1.decklist[3]==self.p2.symbol)and
                (d1.decklist[4]==self.p1.symbol or d1.decklist[4]==self.p2.symbol)and
                (d1.decklist[5]==self.p1.symbol or d1.decklist[5]==self.p2.symbol)and
                (d1.decklist[6]==self.p1.symbol or d1.decklist[6]==self.p2.symbol)and
                (d1.decklist[7]==self.p1.symbol or d1.decklist[7]==self.p2.symbol)and
                (d1.decklist[8]==self.p1.symbol or d1.decklist[8]==self.p2.symbol)):
                print("Game Draw")
                self.p1.draw = self.p1.draw + 1
                self.p2.draw = self.p2.draw +1
                t1.gamedraw()
                return True
        else:
             return False

    def is_game_over(self):
        """checks whether game is over or not"""
        value = t1.is_win()
        if value == self.p1.symbol:
            print("Player:",self.p1.name,"wins the game")
            print(self.p1)
            print(self.p2)
            print("Player 1 entered moves:",d1.player1_choices)
            print("Player 2 entered moves:",d1.player2_choices)
            print("Is player 1 score < player 2 score:",self.p1 < self.p2)
            f=open("Tictactoe","w")
            f.write("   ".join(map(lambda x: str(x), d1.decklist)))

            return True

        elif value == self.p2.symbol:
            print("Player:",self.p2.name,"wins the game")
            print(self.p1)
            print(self.p2)
            print("Player 1 entered moves:",d1.player1_choices)
            print("Player 2 entered moves:",d1.player2_choices)
            print("Is player 1 score < player 2 score:",self.p1 < self.p2)
            f=open("Tictactoe","w")
            f.write("   ".join(map(lambda x: str(x), d1.decklist)))

            return True
        else :
            return False

    def gamedraw(self):
        """after game is daw this function works"""
        print(self.p1)
        print(self.p2)
        lt = ['y', 'n']
        ch = input("do you want to play another game?? press(y/n):")
        if ch == lt[0]:
            t1.new_game()
        else:
            print("Good bye")
            exit(0)

    def validate_user_input1(self,pos1):
        """validate the input of player 1"""
        if pos1<1 or pos1>9:
            print("Move should be between 1 and 9 ","Try again")
            print(d1)
            t1.get_user_input1()

        elif d1.decklist[pos1-1] == self.p1.symbol or d1.decklist[pos1-1]== self.p2.symbol:
            print("Place is already fill","Try another place")
            print(d1)
            t1.get_user_input1()

        else:
            d1.decklist[pos1-1]= self.p1.symbol
            d1.player1_choices.append(pos1)
            print(d1)

            t1.get_user_input2()

    def validate_user_input2(self,pos2):
        """validate the input of player 2"""

        if pos2<1 or pos2>9:
            print("Move should be between 1 and 9 ","Try again")
            print(d1)
            t1.get_user_input2()

        elif d1.decklist[pos2-1] == self.p1.symbol or d1.decklist[pos2-1]== self.p2.symbol:
            print("Place is already fill","Try another place")
            print(d1)
            t1.get_user_input2()

        else:

            d1.decklist[pos2-1]= self.p2.symbol
            d1.player2_choices.append(pos2)
            print(d1)

            t1.get_user_input1()

    def get_user_input1(self):
        """takes input from player 1 and checks the all conditions"""
        if t1.is_game_over() == True:
            lt = ['y', 'n']
            ch = input("do u want to play another game : (y/n)")
            if ch == lt[0]:
                t1.new_game()
            else:
                print("Good bye")
                wait=input("Press enter to continue:")
            pass

        else:
            pos1 = int(input("Enter player1 your move position(between 1 to 9 only):"))
            os.system("cls")
            t1.validate_user_input1(pos1)

    def get_user_input2(self):
        """takes input from player 2 and checks the all conditions"""
        if t1.is_game_over() == True:
            lt = ['y', 'n']
            ch = input("do u want to play another game : (y/n)")
            if ch == lt[0]:
                t1.new_game()
            else:
                print("Good bye")
                wait=input("Press enter to continue:")
            pass

        else:
            pos2 = int(input("Enter player2 your move position(between 1 to 9 only):"))
            os.system("cls")
            t1.validate_user_input2(pos2)


    def start_game(self):
        """game starts from this function"""
        t1.get_user_input1()

    def new_game(self):
        """starts a new game after finish old game"""
        d1.decklist=['1','2','3','4','5','6','7','8','9']
        t1.start_game()


d1 = Deck()
t1 = Tictactoe()
t1.start_game()







