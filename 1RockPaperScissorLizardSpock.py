# rpsls game with gui
from tkinter import *
import random
import time
from tkinter import filedialog
#from tkinter import ttk
#import os
import csv

# global score variables
# wins losses ties gamesPlayed winPercent
win = 0
loss = 0
tie = 0
gamesPlayed = 0
winPercent = 0

# to decides the winner
# called by Rock, Paper, Scissors, Lizard or Spock buttons
# player choice either Rock, Paper, Scissors, Lizard or Spock.
def game(player):

    global win
    global loss
    global tie
    global gamesPlayed
    global winPercent

    # getting the computers choice
    cpu = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    cpu = random.choice(cpu)

    # see who won by comparing picks
    if player == cpu:
        result = 'Tied'
    elif (player == 'Rock' and cpu == 'Paper') or (player == 'Paper' and cpu == 'Scissors') or (player == 'Scissors' and cpu == 'Rock') or (player == 'Rock' and cpu == 'Spock') or (player == 'Paper' and cpu == 'Lizard') or (player == 'Scissors' and cpu == 'Spock') or (player == 'Lizard' and cpu == 'Rock') or (player == 'Lizard' and cpu == 'Scissors') or (player == 'Spock' and cpu == 'Paper') or (player == 'Spock' and cpu == 'Lizard'):
        result = 'Lost'
    else:
        result = 'Won'
    
    # increment ties, losses and games played
    if result == 'Tied':
        tie += 1
        gamesPlayed += 1
    elif result == 'Lost':
        loss += 1
        gamesPlayed += 1
    else:
        win += 1
        gamesPlayed += 1
        
    # calculate the win percent    
    winPercent = int(win)/int(gamesPlayed)*100
    won = str(round(winPercent, 1))
    
    # updated to display the last rounds results and scores
    lbl_result['text'] = f'You {result}!\nYou played {player}, the computer played {cpu}.'
    lbl_score['text'] = f'Score\nGame You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    lbl_gamesPlayed['text'] = f'You have played {gamesPlayed} games.'
    lbl_winPercent['text'] = f'Win Percent: {won}' + '%'

 
 # save function
 # called by save button in the toolbar
def savebox():
    f = filedialog.asksaveasfile(mode='w', initialdir = "/desktop", title = "Select file", filetypes = \
                                 (("text files","*.txt"),("all files","*.*")))
    if f is None:
        return
    f.write(f'{win},{loss},{tie},{gamesPlayed},{winPercent}')

 # load game function
 # called by load toolbar button
def load():
    global win
    global loss
    global tie
    global gamesPlayed
    global winPercent

    s = filedialog.askopenfilename(initialdir = "/desktop",title = "Select file",filetypes = \
                                   (("text files","*.txt"),("all files","*.*")))
    with open(s, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for data in csv_reader:
            data = [float(x) for x in data]
    win = int(data[0])
    loss = int(data[1])
    tie = int(data[2])
    gamesPlayed = int(data[3])
    winPercent = round(data[4], 1)
    file.close()
    lbl_score['text'] = f'Score\nGame You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    lbl_result['text'] = 'Have Fun!'
    lbl_gamesPlayed['text'] = f'Games Played: {gamesPlayed}'
    lbl_winPercent['text'] = f'Win Percent: {winPercent}' + '%'
    
# resets the score, called by the reset toolbar button thingy
# sets win loss tie gamesPlayed and winPercent to zero then updates the labels
def reset():
    global win
    global loss
    global tie
    global gamesPlayed
    global winPercent
    win = 0
    loss = 0
    tie = 0
    gamesPlayed = 0
    winPercent = 0
    
    lbl_score['text'] = f'Score\nGame You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    lbl_result['text'] = 'Have Fun!\nGet Ready to Play!'
    lbl_gamesPlayed['text'] = f'Games Played: {gamesPlayed}'
    lbl_winPercent['text'] = f'Win Percent: {winPercent}' + '%'

# configure and update the clock
def update_clock():
        now = time.strftime("%I:%M:%S %p \n%A %b %d, %Y")
        clock.configure(text=now)
        root.after(1000, update_clock)
        
# set the gui
root = Tk()

# window properties - size and where to open
root.wm_geometry("600x300-500+400")
root.wm_title("Rock Paper Scissors Lizard Spock")

# adding the toolbar
menu = Menu(root)
root.config(menu=menu)
menu.add_command(label='Save', command=savebox)
menu.add_command(label='Load', command=load)
menu.add_command(label='Reset', command=reset)
menu.add_cascade(label='Exit', command=root.destroy)

# cutting window into two frames
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# text, the title the result and the score
lbl_title = Label(topframe, text='Rock Paper Scissors Lizard Spock', font=('Courier New', 20, 'bold'))
lbl_title.pack()

lbl_result = Label(topframe, text='Have Fun!\nGet Ready to Play!', font=('Comic Sans MS', 10, 'bold'))
lbl_result.pack()

lbl_score = Label(topframe, text='Score\nGame You Won: 0\nGames Computer Won: 0\nTies: 0', font=('Comic Sans MS', 10, 'bold'))
lbl_score.pack()

lbl_gamesPlayed = Label(topframe, text='Games Played: 0', font=('Comic Sans MS', 10, 'bold'))
lbl_gamesPlayed.pack()

lbl_winPercent = Label(topframe, text='Win Percent: 0' + '%', font=('Comic Sans MS', 10, 'bold'))
lbl_winPercent.pack()


# buttons, Rock, Paper, Scissors, Lizard and Spock
btn_rock = Button(bottomframe, text='Rock', bg='grey', command=lambda: game('Rock'))
btn_rock.grid(row=0, column=0, padx=(20, 20))

btn_paper = Button(bottomframe, text='Paper', bg='white', command=lambda: game('Paper'))
btn_paper.grid(row=0, column=1, padx=(20, 20))

btn_scissors = Button(bottomframe, text='Scissors', bg='silver', command=lambda: game('Scissors'))
btn_scissors.grid(row=0, column=2, padx=(20, 20))

btn_lizard = Button(bottomframe, text='Lizard', bg='light green', command=lambda: game('Lizard'))
btn_lizard.grid(row=0, column=3, padx=(20, 20))

btn_spock = Button(bottomframe, text='Spock', bg='light blue', command=lambda: game('Spock'))
btn_spock.grid(row=0, column=4, padx=(20, 20))

# making blank space at bottom of window
lbl_blank = Label(bottomframe, text='')
lbl_blank.grid(row=1)

# configure and place the clock
clock = Label(text="", fg="Black", font=("Comic Sans", 8, 'bold'))
clock.pack(side=BOTTOM)
update_clock()
      
root.mainloop()
