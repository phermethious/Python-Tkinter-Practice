#5/16/2023
# rpsls game with gui
from tkinter import *
import random
import time
from tkinter import filedialog
from tkinter import messagebox
#from tkinter import ttk
import os
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
    elif (player == 'Rock' and cpu == 'Paper') or (player == 'Paper' and cpu == 'Scissors') or \
    (player == 'Scissors' and cpu == 'Rock') or (player == 'Rock' and cpu == 'Spock') or \
    (player == 'Paper' and cpu == 'Lizard') or (player == 'Scissors' and cpu == 'Spock') or \
    (player == 'Lizard' and cpu == 'Rock') or (player == 'Lizard' and cpu == 'Scissors') or \
    (player == 'Spock' and cpu == 'Paper') or (player == 'Spock' and cpu == 'Lizard'):
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
    
    # added the funny sayings to go with the choices
    sayings = {
        1: "Rock crushes Lizard...",
        2: "Scissors cuts Paper...",
        3: "Paper covers Rock...",
        4: "Lizard Poisons Spock...",
        5: "Spock smashes Scissors...",
        6: "Scissors decapitates Lizard...",
        7: "Lizard eats Paper...",
        8: "Paper disproves Spock...",
        9: "Spock vaporizes Rock...",
        10: "Rock crushes Scissors...",
        11: "Tie Game!"} 
    
    if (player == 'Rock' and cpu == 'Lizard') or (cpu == 'Rock' and player == 'Lizard'):
        display = sayings[1]
    elif (player == 'Scissors' and cpu == 'Paper') or (cpu == 'Scissors' and player == 'Paper'):
        display = sayings[2]
    elif (player == 'Paper' and cpu == 'Rock') or (cpu == 'Paper' and player == 'Rock'):
        display = sayings[3]
    elif (player == 'Lizard' and cpu == 'Spock') or (cpu == 'Lizard' and player == 'Spock'):
        display = sayings[4]
    elif (player == 'Spock' and cpu == 'Scissors') or (cpu == 'Spock' and player == 'Scissors'):
        display = sayings[5]
    elif (player == 'Scissors' and cpu == 'Lizard') or (cpu == 'Scissors' and player == 'Lizard'):
        display = sayings[6]
    elif (player == 'Lizard' and cpu == 'Paper') or (cpu == 'Lizard' and player == 'Paper'):
        display = sayings[7]
    elif (player == 'Paper' and cpu == 'Spock') or (cpu == 'Paper' and player == 'Spock'):
        display = sayings[8]
    elif (player == 'Spock' and cpu == 'Rock') or (cpu == 'Spock' and player == 'Rock'):
        display = sayings[9]
    elif (player == 'Rock' and cpu == 'Scissors') or (cpu == 'Rock' and player == 'Scissors'):
        display = sayings[10]
    else:
        display = sayings[11]   
 
    # updated to display the last rounds results and scores
    lbl_result['text'] = f'You {result}! You played {player}, the computer played {cpu}.'
    lbl_sayings['text'] = f'{display}'
    lbl_score['text'] = f'Score\nGame You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    lbl_gamesPlayed['text'] = f'You have played {gamesPlayed} games.'
    lbl_winPercent['text'] = f'Win Percent: {won}' + '%'
    
 # save function
 # called by save button in the toolbar
def savebox():
    saveFile = filedialog.asksaveasfile(mode='w', initialdir = "/desktop", title = "Select file", filetypes = \
                                 (("text files","*.txt"),("all files","*.*")))
    if saveFile is None:
        return
    saveFile.write(f'{win},{loss},{tie},{gamesPlayed},{winPercent}')

 # load game function
 # called by load toolbar button
def load():
    global win
    global loss
    global tie
    global gamesPlayed
    global winPercent

    loadFile = filedialog.askopenfilename(initialdir = "/desktop",title = "Select file",filetypes = \
                                   (("text files","*.txt"),("all files","*.*")))
    with open(loadFile, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for data in csv_reader:
            data = [float(x) for x in data]
    win = int(data[0])
    loss = int(data[1])
    tie = int(data[2])
    gamesPlayed = int(data[3])
    winPercent = round(data[4], 1)
    file.close()
    lbl_score['text'] = f'Score\nGames You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    #lbl_result['text'] = 'I Hope You have Fun!\nGet Ready to Play!'
    lbl_gamesPlayed['text'] = f'Games Played: {gamesPlayed}'
    lbl_winPercent['text'] = f'Win Percent: {winPercent}' + '%'
    
# resets the score, called by the reset toolbar button
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
    
    lbl_score['text'] = f'Score\nGames You Won: {win}\nGames Computer Won: {loss}\nTies: {tie}'
    lbl_result['text'] = 'I Hope You have Fun Playing!'
    lbl_sayings['text'] = ''
    lbl_gamesPlayed['text'] = f'Games Played: {gamesPlayed}'
    lbl_winPercent['text'] = f'Win Percent: {winPercent}' + '%'

# configure and update the clock
def update_clock():
        now = time.strftime("%I:%M:%S %p \n%A %b %d, %Y")
        clock.configure(text=now)
        window.after(1000, update_clock)

def aboutmessage():
    messagebox.showinfo('About Rock Paper Scissor Lizard Spock', 'This game was developed by: BLW. I hope you \
    enjoy playing it as much as I enjoyed writing it.\n\n\nCopyright: \xa9 2023')
        
# set the gui
window = Tk()

#change icon
#window.iconbitmap(r'ENTER PATH TO ICON')

# window properties - size and where to open
window.geometry("650x350-700+400")
window.title("Rock Paper Scissors Lizard Spock")

# prevent the window from being resized
window.resizable(0, 0)

# adding the menubar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Save', command=savebox)
filemenu.add_command(label='Load', command=load)
filemenu.add_command(label='Reset', command=reset)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About...', command=aboutmessage)
menubar.add_cascade(label='Help', menu=helpmenu)
    
# cutting window into two frames
topframe = Frame(window)
topframe.pack()
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

# text, title, result, sayings, score gamesPlayed and winPercent
lbl_title = Label(topframe, text='Rock Paper Scissors Lizard Spock', font=('Courier New', 20, 'bold'))
lbl_title.pack()

lbl_result = Label(topframe, text='I Hope You have Fun Playing!', font=('Comic Sans MS', 10, 'bold'))
lbl_result.pack()

lbl_sayings = Label(topframe, text='', fg='Red', font=('Comic Sans MS', 10, 'bold'))
lbl_sayings.pack()

lbl_score = Label(topframe, text='Score\nGames You Won: 0\nGames Computer Won: 0\nTies: 0', \
                  font=('Comic Sans MS', 10, 'bold'))
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
 
window.config(menu=menubar)     
window.mainloop()
