import os
import sqlite3
from tkinter import messagebox
from tkinter import *

class Player:
    """represents a players of game and results"""

    def __init__(self,data_access,id):
        """Constructor that initialze the values"""
        d1 = data_access.get_player_score(id)
        self.won = d1[3]
        self.lost = d1[5]
        self.draw = d1[4]
        self.name = d1[1]
        self.id = d1[0]
        self.playing_mark = d1[2]
        self.statistics = {'Won':self.won,'Lost':self.lost,'draw':self.draw}

    def get_score(self):
        """update the score"""
        return (self.won*2)+self.draw-self.lost

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

class DataAccessLayer:
    '''this is class that will handle the database  '''

    def __init__(self):
        self.conn = sqlite3.connect('tic_tac_toe.db')
        self.cur = self.conn.cursor()

    def get_player_score(self,id):
        ''' method to get score from database'''
        self.cur.execute("SELECT * FROM Player where PlayerId ='%d'"%id)
        data = self.cur.fetchone()
        return(data)

    def save_player_data(self,id,win,lose,draw):
        '''method to save data to database'''
        self.cur.execute("Update Player SET Won=%d,Drawn=%d,Lost=%d WHERE PlayerId=%d"%(win,draw,lose,id))
        self.conn.commit()

    def __del__(self):
        ''' destructor that will destroy the connection object'''
        self.conn.close()

class tictactoe:

    def __init__(self,root):
        ''' constructor that will initiate all the following values and objects'''
        self.dict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        self.turn = 0
        self.data_access = DataAccessLayer()
        self.p1 = Player(self.data_access,1)
        self.p2 = Player(self.data_access,2)
        self.game_counter = 1
        self.d1 = Deck()

        root.title("Tic Tac Toe")
        root.geometry("300x500")
        self.r1 = root
        self.status_frame1 = Frame(root,bg="white",width=300,height=50)
        self.status_frame1.pack()
        self.v1 = StringVar()
        self.msg1 = "Player 1 \n"+str(self.p1.get_score())
        self.label_p1_score = Label(self.status_frame1,text=self.msg1,textvariable=self.v1).pack(side=LEFT)
        self.v2 = StringVar()
        self.msg2 = "     Game no:\n"+str(self.game_counter)
        self.label_counter = Label(self.status_frame1,text=self.msg2,textvariable=self.v2).pack(side=LEFT)
        self.v3 = StringVar()
        self.msg3 = "     Player2 \n"+str(self.p2.get_score())
        self.label_p2_score = Label(self.status_frame1,text=self.msg3,textvariable=self.v3).pack(side=LEFT)

        self.c1 = Canvas(root,width=300,height=400)
        self.c1.pack()
        self.w2 = Frame(root,bg="white",width=300,height=100)
        self.w2.pack()
        self.v = StringVar()
        self.label_msg = Label(self.w2,textvariable = self.v).pack(side=TOP)
        self.c1.create_line(100,50,100,350,width=4,fill="blue")
        self.c1.create_line(200,50,200,350,width=4,fill="blue")
        self.c1.create_line(0,150,300,150,width=4,fill="blue")
        self.c1.create_line(0,250,300,250,width=4,fill="blue")

        self.start_game()
        root.mainloop()

    def is_game_over(self):
        ''' method that check that game is over or not and display the message'''
        if(self.dict['1']==self.dict['2'] and self.dict['1']==self.dict['3'] and self.dict['1']!=0):
            if(self.dict['1']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check=='yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['1']==self.dict['5'] and self.dict['1']==self.dict['9'] and self.dict['1']!=0):
            if(self.dict['1']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['1']==self.dict['4'] and self.dict['1']==self.dict['7'] and self.dict['1']!=0):
            if(self.dict['1']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['3']==self.dict['6'] and self.dict['3']==self.dict['9'] and self.dict['3']!=0):
            if(self.dict['3']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['3']==self.dict['5'] and self.dict['3']==self.dict['7'] and self.dict['3']!=0):
            if(self.dict['3']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['4']==self.dict['5'] and self.dict['4']==self.dict['6'] and self.dict['4']!=0):
            if(self.dict['4']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['7']==self.dict['8'] and self.dict['7']==self.dict['9'] and self.dict['7']!=0):
            if(self.dict['7']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['2']==self.dict['5'] and self.dict['2']==self.dict['8'] and self.dict['2']!=0):
            if(self.dict['2']==1):
                self.p1.won += 1
                self.p1.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player1 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
            else:
                self.p2.won += 1
                self.p2.lost -= 1
                self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
                self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
                check = messagebox.askquestion(title="Game over",message="player2 won!, start new game?")
                if check == 'yes':
                    self.new_game()
                else:
                    quit(self.r1)
        elif(self.dict['1']!=0 and self.dict['2']!=0 and self.dict['3']!=0 and self.dict['4']!=0 and self.dict['5']!=0 and
             self.dict['6']!=0 and self.dict['7']!=0 and self.dict['8']!=0 and self.dict['9']!=0):
            self.p1.draw += 1
            self.p2.draw += 1
            self.data_access.save_player_data(self.p1.id,self.p1.won,self.p1.lost,self.p1.draw)
            self.data_access.save_player_data(self.p2.id,self.p2.won,self.p2.lost,self.p2.draw)
            check = messagebox.askquestion(title="Game over",message="Game draw!, start a new game?")
            if check == 'yes':
                self.new_game()
            else:
                quit(self.r1)

    def button_click1(self,event):
        ''' method that draw marks by clicking on the canvas '''

        if self.turn == 0:

            if event.x > 0 and event.x < 100 and event.y >50 and event.y<150:

                if self.dict['1']==0:
                    self.c1.create_oval(25,75,75,125,width=4,outline="black")
                    self.v.set("Cell 1 is selected by player 1")
                    self.dict['1']=1
                    self.turn = 1

                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 0 and event.x < 100 and event.y >150 and event.y<250:

                if self.dict['4']==0:
                    self.c1.create_oval(25,175,75,225,width=4,outline="black")
                    self.v.set("Cell 4 is selected by player 1")
                    self.dict['4']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 0 and event.x < 100 and event.y >250 and event.y<350:

                if self.dict['7']==0:
                    self.c1.create_oval(25,275,75,325,width=4,outline="black")
                    self.v.set("Cell 7 is selected by player 1")
                    self.dict['7']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")

            elif event.x > 100 and event.x < 200 and event.y >50 and event.y<150:

                if self.dict['2']==0:
                    self.c1.create_oval(125,75,175,125,width=4,outline="black")
                    self.v.set("Cell 2 is selected by player 1")
                    self.dict['2']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 100 and event.x < 200 and event.y >150 and event.y<250:

                if self.dict['5']==0:
                    self.c1.create_oval(125,175,175,225,width=4,outline="black")
                    self.v.set("Cell 5 is selected by player 1")
                    self.dict['5']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 100 and event.x < 200 and event.y >250 and event.y<350:

                if self.dict['8']==0:
                    self.c1.create_oval(125,275,175,325,width=4,outline="black")
                    self.v.set("Cell 8 is selected by player 1")
                    self.dict['8']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 200 and event.x < 300 and event.y >50 and event.y<150:

                if self.dict['3']==0:
                    self.c1.create_oval(225,75,275,125,width=4,outline="black")
                    self.v.set("Cell 3 is selected by player 1")
                    self.dict['3']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 200 and event.x < 300 and event.y >150 and event.y<250:

                if self.dict['6']==0:
                    self.c1.create_oval(225,175,275,225,width=4,outline="black")
                    self.v.set("Cell 6 is selected by player 1")
                    self.dict['6']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 200 and event.x < 300 and event.y >250 and event.y<350:

                if self.dict['9']==0:
                    self.c1.create_oval(225,275,275,325,width=4,outline="black")
                    self.v.set("Cell 9 is selected by player 1")
                    self.dict['9']=1
                    self.turn = 1
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")


        else:
            if event.x >0 and event.x < 100 and event.y >50 and event.y<150:

                if self.dict['1']==0:
                    self.c1.create_line(25,75,75,125,width=4,fill="black")
                    self.c1.create_line(75,75,25,125,width=4,fill="black")
                    self.v.set("Cell 1 is selected by player 2")
                    self.dict['1']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 0 and event.x < 100 and event.y >150 and event.y<250:

                if self.dict['4']==0:
                    self.c1.create_line(25,175,75,225,width=4,fill="black")
                    self.c1.create_line(75,175,25,225,width=4,fill="black")
                    self.v.set("Cell 4 is selected by player 2")
                    self.dict['4']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 0 and event.x < 100 and event.y >250 and event.y<350:

                if self.dict['7']==0:
                    self.c1.create_line(25,275,75,325,width=4,fill="black")
                    self.c1.create_line(75,275,25,325,width=4,fill="black")
                    self.v.set("Cell 7 is selected by player 2")
                    self.dict['7']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 100 and event.x < 200 and event.y >50 and event.y<150:

                if self.dict['2']==0:
                    self.c1.create_line(125,75,175,125,width=4,fill="black")
                    self.c1.create_line(175,75,125,125,width=4,fill="black")
                    self.v.set("Cell 2 is selected by player 2")
                    self.dict['2']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 100 and event.x < 200 and event.y >150 and event.y<250:

                if self.dict['5']==0:
                    self.c1.create_line(125,175,175,225,width=4,fill="black")
                    self.c1.create_line(175,175,125,225,width=4,fill="black")
                    self.v.set("Cell 5 is selected by player 2")
                    self.dict['5']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 100 and event.x < 200 and event.y >250 and event.y<350:

                if self.dict['8']==0:
                    self.c1.create_line(125,275,175,325,width=4,fill="black")
                    self.c1.create_line(175,275,125,325,width=4,fill="black")
                    self.v.set("Cell 8 is selected by player 2")
                    self.dict['8']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 200 and event.x < 300 and event.y >50 and event.y<150:

                if self.dict['3']==0:
                    self.c1.create_line(225,75,275,125,width=4,fill="black")
                    self.c1.create_line(275,75,225,125,width=4,fill="black")
                    self.v.set("Cell 3 is selected by player 2")
                    self.dict['3']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")

            elif event.x > 200 and event.x < 300 and event.y >150 and event.y<250:

                if self.dict['6']==0:
                    self.c1.create_line(225,175,275,225,width=4,fill="black")
                    self.c1.create_line(275,175,225,225,width=4,fill="black")
                    self.v.set("Cell 6 is selected by player 2")
                    self.dict['6']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")
            elif event.x > 200 and event.x < 300 and event.y >250 and event.y<350:

                if self.dict['9']==0:
                    self.c1.create_line(225,275,275,325,width=4,fill="black")
                    self.c1.create_line(275,275,225,325,width=4,fill="black")
                    self.v.set("Cell 9 is selected by player 2")
                    self.dict['9']=2
                    self.turn = 0
                    self.is_game_over()
                else:
                    self.v.set("Cell position is already selected")



    def get_user_input(self):
        '''method that get the user input'''
        self.c1.bind("<ButtonPress-1>",self.button_click1)

    def start_game(self):
        '''method from that game will start'''
        msg1 = "Player 1 \n"+str(self.p1.get_score())
        msg2 = "     Game no:\n"+str(self.game_counter)
        msg3 = "     Player 2 \n"+str(self.p2.get_score())
        self.v1.set(msg1)
        self.v2.set(msg2)
        self.v3.set(msg3)
        self.get_user_input()

    def new_game(self):
        '''method that will execute to play another game'''
        self.game_counter += 1
        self.c1.delete(ALL)
        self.dict = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
        self.v.set("No Cell position is selected")
        self.turn = 0
        self.c1.create_line(100,50,100,350,width=4,fill="blue")
        self.c1.create_line(200,50,200,350,width=4,fill="blue")
        self.c1.create_line(0,150,300,150,width=4,fill="blue")
        self.c1.create_line(0,250,300,250,width=4,fill="blue")

        self.start_game()


root = Tk()

t1 = tictactoe(root)

root.mainloop()









