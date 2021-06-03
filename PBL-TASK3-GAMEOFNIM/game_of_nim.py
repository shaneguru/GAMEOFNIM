import random
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
from timeit import default_timer as timer

# https://en.wikipedia.org/wiki/Nim
# https://en.wikipedia.org/wiki/Minimax
# https://github.com/NGoutcher/nim-game-ai/blob/357a2eaefaf37c9d0d144334e976c9c473a7a050/nimgame.py
# https://github.com/islammohsen/NimGame-Python/blob/master/project.py

#Creating the main frame for GUI
mainframe = Tk()
mainframe.title("Game of Nim")
mainframe.geometry('500x400')
mainframe.configure(background='#2980b9')

# Creating global variables for game state which will be a tuple, number of piles and number of sticks since it should be accessed from everywhere
global game_state, num_piles, num_pieces

#Creating variables which will go into the starting GUI
sliderPilesNum = tkinter.IntVar()
sliderPilesEnt = tkinter.StringVar()
sliderPilesEnt.set('Select Amount of Piles')

sliderMaxNum = tkinter.IntVar()
sliderMaxNumEnt = tkinter.StringVar()
sliderMaxNumEnt.set('Select the maximum amount in a pile')

nimSum = tkinter.StringVar()
miniMax = tkinter.StringVar()

selectBot = tkinter.StringVar()
selectBot.set('Which Bot? Nimsum(Normal) | Minimax(misère)')

selectPlay = tkinter.StringVar()
selectPlay.set('Do you want to play first or second?')
GameLogs = StringVar()
PileNumber = StringVar()
RemoveCount = StringVar()
logs = None
FinalImage = None

#These will be the pictures that will be used dots1-7 are the max number of pieces that can go into one pile
Img = []
log_eve = []
# list containg image pathes
Pathes = ["assets/Empty.png",
          "assets/dots1.png",
          "assets/dots2.png",
          "assets/dots3.png",
          "assets/dots4.png",
          "assets/dots5.png",
          "assets/dots6.png",
          "assets/dots7.png"]
winImg = "assets/YouWin.png"
loseImg = "assets/Gameover.png"

Pag1 = None
Page2 = None
frame5 = None


#function to create the initial game state it will select a random number from 1 to user desired number to all the piles
def createState(num_piles, max_sticks):
    piles = []
    for i in range(0, num_piles):
        rand = random.randint(1, max_sticks)
        piles.append(rand)
    return piles

#this function initilizes the game by creating the initial game state according to the users preferences
def create_game():
    global num_piles, max_sticks, piles, game_state, bottype
    num_piles = int(sliderPilesNum.get())
    max_sticks = int(sliderMaxNum.get())
    if nimSum.get() is None:
        bottype = miniMax.get()
    else:
        bottype = nimSum.get()
    piles = createState(num_piles, max_sticks)
    game_state = (piles, 1)
    for i in range(0, num_piles):
        AddImage(frame2, Pathes[piles[i]])

    Page1.pack_forget()
    mainframe.geometry("1920x1240")
    Page2.pack()

#This section will have all the properties which will go into the start page (labels, scales, buttons)
Page1 = Frame(mainframe)
Page1.pack()
Page1.config(bg="#2980b9")


ttk.Label(
    Page1,
    textvariable='',
    background='#2980b9').grid(
        column=1,
        row=4,
    columnspan=5)
ttk.Label(
    Page1,
    textvariable=sliderPilesEnt,
    background='#bdc3c7').grid(
        column=1,
        row=8,
    columnspan=5)
tkinter.Scale(
    Page1,
    from_=1,
    to_=6,
    length=300,
    bg='#bdc3c7',
    orient='horizontal',
    variable=sliderPilesNum).grid(
        column=1,
        row=12,
    columnspan=5)

ttk.Label(
    Page1,
    textvariable='',
    background='#2980b9').grid(
        column=1,
        row=14,
    columnspan=5)
ttk.Label(
    Page1,
    textvariable=sliderMaxNumEnt,
    background='#bdc3c7').grid(
        column=1,
        row=16,
    columnspan=5)
tkinter.Scale(
    Page1,
    from_=1,
    to_=7,
    length=300,
    bg='#bdc3c7',
    orient='horizontal',
    variable=sliderMaxNum).grid(
        column=1,
        row=20,
    columnspan=5)

ttk.Label(
    Page1,
    textvariable='',
    background='#2980b9').grid(
        column=1,
        row=26,
    columnspan=5)

ttk.Label(
    Page1,
    textvariable=selectBot,
    background='#bdc3c7').grid(
        column=1,
        row=28,
    columnspan=5)
Radiobutton(
    Page1,
    text="NIMSUM",
    variable=nimSum,
    value="NIMSUM",
    indicator=0,
    background="light blue").grid(
        column=0,
        row=30,
    columnspan=4)
Radiobutton(
    Page1,
    text="MINIMAX",
    variable=miniMax,
    value="MINIMAX",
    indicator=0,
    background="light blue").grid(
        column=3,
        row=30,
    columnspan=5)

ttk.Label(
    Page1,
    textvariable='',
    background='#2980b9').grid(
        column=1,
        row=34,
    columnspan=5)
tkinter.Button(
    Page1,
    text="START GAME",
    command=create_game,
    width=22,
    height=8,
    background='#bdc3c7').grid(
        column=1,
        row=36,
    columnspan=5)

Page2 = Frame(mainframe)
Page2.config(bg="#2980b9")

frame1 = Frame(Page2)
frame1.pack(pady=(50, 0))

welcome_label = Label(frame1,
                      bg='#bdc3c7',
                      justify=CENTER,
                      text="Can you beat the bot?",
                      font=("Arial", 35))
welcome_label.pack()

# add pile images
frame2 = Frame(Page2)
frame2.pack(pady=(50, 0))
frame2.config(bg="#2980b9")

#this function adds the dot images according the game state ie. if the game state (2,3) it will add the picture with 2 dots and 3 dots
def AddImage(frame, path):
    Photo = ImageTk.PhotoImage(Image.open(path))
    newImage = Label(frame2,
                     image=Photo,
                     bd=5,
                     relief="groove", bg="#2980b9")
    newImage.image = Photo
    newImage.pack(side=LEFT)
    Img.append(newImage)

#frame for inputting user inputs selecting pile and number of pieces to remove
frame3 = Frame(Page2)
frame3.pack(pady=(50, 0))
frame3.config(bg="#2980b9")

pile_number = Label(frame3,
                    text="Enter Pile Number",
                    font=("bold"))
pile_number.pack(side=LEFT)

entry_1 = Entry(frame3,
                bd=5,
                textvariable=PileNumber)
entry_1.pack(side=LEFT)

amount_removed = Label(frame3,
                       text="Enter number of balls to be removed",
                       font=("bold"))
amount_removed.pack(side=LEFT)

entry_2 = Entry(frame3,
                bd=5,
                textvariable=RemoveCount)
entry_2.pack(side=LEFT)


# this function updates the pile after a move was made
def UpdatePile(Index, value, state):
    game_state[0][Index] -= value

    if game_state[0][Index] == 0:
        game_state[0].remove(0)

    for widget in frame2.winfo_children():
        widget.destroy()
    for i in range(0, len(state[0])):
        AddImage(frame2, Pathes[state[0][i]])

# this function updates the pile after a move was made for minimax
def UpdatePileMiniMax(state):
    for widget in frame2.winfo_children():
        widget.destroy()
    for i in range(0, len(state[0])):
        AddImage(frame2, Pathes[state[0][i]])

# this function updates the pile the user clicks on the restart button
def ResUpdatePile(Index, pile):
    NewPhoto = ImageTk.PhotoImage(Image.open(Pathes[pile[0][Index]]))
    Img[Index].config(image=NewPhoto)
    Img[Index].image = NewPhoto



# this function handles log events - this will be displayed in frame 5 - it will display moves made and etc.
def AddLogEvent(CurrentEvent):
    log_eve.append(CurrentEvent)
    GameLogs.set("")
    LogsSize = len(log_eve)
    if LogsSize <= 20:
        for LogEvent in log_eve:
            GameLogs.set(GameLogs.get() + LogEvent + '\n')
    else:
        for i in range(LogsSize - 20, LogsSize):
            GameLogs.set(GameLogs.get() + log_eve[i] + '\n')


# bit 2^(largest - 1) : Largest number position
def larg_val(largest):
    if largest == 0:
        return -1
    maxx = 0
    pos = -1
    num = pow(2, largest - 1)
    for i in range(0, len(game_state[0])):
        if (int(game_state[0][i]) & int(num)) and (game_state[0][i] > maxx):
            pos = i
            maxx = game_state[0][i]
    return pos

# this function choses the optimal move using nimsum - it will calculate the cumulative nim sum
# it will select the pile which will have a less number than the nimsum when substracted by it
def nimsum_bot():
    XOR_val = 0
    global taking_pieces, pile_pos
    for i in range(0, len(game_state[0])):
        XOR_val = XOR_val ^ game_state[0][i]
    temp = XOR_val
    largest = 0
    while temp != 0:
        temp = temp // 2
        largest = largest + 1
    pile_pos = larg_val(largest)
    taking_pieces = 0
    if pile_pos == -1:
        for i in range(0, 1):
            if game_state[0][i] == 0:
                continue
            random.seed(datetime.now())
            num = random.randint(1, game_state[0][i])
            taking_pieces = num
            pile_pos = i
    else:
        taking_pieces = game_state[0][pile_pos] - (game_state[0][pile_pos] ^ XOR_val)

#this function is the max player in minmax it will find the best max move using alpha pruning
def max_player(state, alpha, beta):
    global game_state
    if terminal_test(state):
        return utility(state)
    v = float("-inf")
    node = state
    for s in successors(state):
        vp = min_player(s, alpha, beta)
        if vp > v:
            v = vp
            node = s
        if vp >= beta:
            if terminal_test(s):
                return utility(s)
            return v
        if vp > alpha:
            alpha = vp
    game_state = node
    return v


#this function is the min player in minmax it will find the best min move using alpha pruning
def min_player(state, alpha, beta):
    global game_state
    if terminal_test(state):
        return utility(state)
    v = float("inf")
    node = state
    for s in successors(state):
        vp = max_player(s, alpha, beta)
        if vp < v:
            v = vp
            node = s
        if vp <= alpha:
            if terminal_test(s):
                return utility(s)
            return v
        if vp < beta:
            beta = vp
    game_state = node
    return v

#list of states than can be reached from the current position
def successors(state):
    l = []
    ind = 0
    player = state[-1]
    if player == 1:
        player = 2
    else:
        player = 1

    for pile in state[0]:
        number = 1
        while number < 4:
            if pile - number == 0:
                temp = state[0][:]
                temp.remove(pile)
                l.append((temp, player))

            if pile - number > 0:
                temp = state[0][:]
                temp[ind] = pile - number
                l.append((temp, player))
            number += 1
        ind += 1
    return l

# this is the numerical value assigned to each terminal state
def utility(state):
    if state[-1] == 1:
        return 1
    elif state[-1] == 2:
        return -1

# the terminal_test function checks if the game is over
def terminal_test(state):
    if state[0] == []:
        return True
    else:
        return False

# load final image
def LoadFinalImage(PlayerWin):
    Photo = None
    if PlayerWin:
        Photo = ImageTk.PhotoImage(Image.open(winImg))
    else:
        Photo = ImageTk.PhotoImage(Image.open(loseImg))
    FinalImage.config(
        image=Photo)
    FinalImage.config(height="300")
    FinalImage.image = Photo
    FinalImage.pack()


# handling the user inputs
def ExceptionInvalidInput():
    messagebox.showerror("Error", "Please, enter a valid input.")

'''

PERFORMS THE GAME PLAY

'''
def user_input():
    global PileNumber, RemoveCount, game_state
    try:
        ind = int(PileNumber.get()) - 1
        value = int(RemoveCount.get())
    except BaseException:
        ExceptionInvalidInput()
        return

    if ind >= 0 and ind < len(
            game_state[0]) and value > 0 and value <= game_state[0][ind]:
        frame5.pack(pady=(20, 0))
        AddLogEvent("Player took " + str(value) +
                    " circles from pile " + str(ind + 1))
        PileNumber.set(""), RemoveCount.set("")
        UpdatePile(ind, value, game_state)
        game_state = (game_state[0], 2)
        if terminal_test(game_state):
            GameLogs.set("")
            logs.pack_forget()
            if(bottype == 'NIMSUM'):
                LoadFinalImage(True)
            else:
                LoadFinalImage(False)
            return
        if(bottype == 'NIMSUM'):
            start = timer()
            nimsum_bot()
            end = timer()
            AddLogEvent("Computer took " + str(taking_pieces) +
                        " circles from pile " + str(pile_pos + 1))
            UpdatePile(pile_pos, taking_pieces, game_state)
            AddLogEvent("State after bots move:" + str(game_state[0]))
            AddLogEvent("Time taken for nimsum: {:0.5f}sec".format(end-start) + "s")
        else:
            start = timer()
            min_player(game_state, float("-inf"), float("inf"))
            end = timer()
            UpdatePileMiniMax(game_state)
            AddLogEvent("State after bots move:" + str(game_state[0]))
            AddLogEvent("Time taken for minimax: {:0.5f}sec".format(end - start) + "s")

        if terminal_test(game_state):
            GameLogs.set("")
            logs.pack_forget()
            if(bottype == 'NIMSUM'):
                LoadFinalImage(False)
            else:
                LoadFinalImage(True)
    else:
        ExceptionInvalidInput()


def user_restart():
    global log_eve, num_piles, max_sticks, game_state
    piles = createState(num_piles, max_sticks)
    game_state = (piles, 1)
    log_eve = []
    PileNumber.set("")
    RemoveCount.set("")
    FinalImage.pack_forget()
    logs.pack()
    frame5.pack_forget()
    UpdatePileMiniMax(game_state)


frame4 = Frame(Page2)
frame4.pack(pady=(50, 0))
frame4.config(bg="#2980b9")

button_enter = Button(frame4, text="Play",

                      command=user_input,
                      font=("Arial", 10, 'bold'),
                      background='#bdc3c7',
                      width=10,
                      height=2)
button_restart = Button(frame4,
                        text="Restart",
                        command=user_restart,
                        background='#bdc3c7',
                        font=("Arial", 10, 'bold'),
                        width=10,
                        height=2)

button_enter.pack(side=LEFT,
                  padx=(0, 50))
button_restart.pack(side=LEFT)


frame5 = Frame(Page2)
frame5.config(bg="#2980b9", height='20')
logs = Label(frame5,
             bg='#2980b9',
             textvariable=GameLogs,
             relief="groove", height='20')
logs.pack()
FinalImage = Label(frame5)

mainframe.mainloop()
