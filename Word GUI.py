#import needed modules
from tkinter import *
import random

#read dictionary
dic = open('Dictionary.txt')
dic = dic.read()
dic = dic.split('\n')

#initialize variables
total = 0
wordscore = ''
anscol = 'blue'

#function to create random letter sequences
def getlets():
    
    #defining variables
    global scramble
    doit = True
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vowels = 'AEIOU'
    chars = random.randint(5,10)
    scramble = ''

    #making a random letter sequence
    for i in range(chars):
        let = random.randint(0,25)
        scramble += alph[let]
        
    #making sure there is a vowel in the sequence
    for i in scramble:
        if i in vowels:
            doit = False
            break
    if doit == True:
        return getlets()

    #displaying results
    label3['text'] = scramble
    guess.delete(0,'end')
    
    leave()


#function to check if a word is valid
def check(*discard):

    #defining variables
    global wordscore, dic, scramble, word, total, anscol
    word = guess.get()
    val = True
    wordscore = 0

    #checking if the submitted word can be made with the provided letters
    for i in word:
        if word.count(i) > scramble.count(i):
            val = False

    #checking if the submitted word is an actual word
    if word not in dic:
        val = False

    #do the following if the word is valid
    if val == True and len(word) != 0:

        #determine score
        wordscore = len(word)**2

        #add score to total
        total += wordscore

        #prepare to display the points earned
        wordscore = '+ ' + str(wordscore) + ' points'
        anscol = 'lightgreen'

    #do the following if the word is not valid
    if val == False:
        
        #prepare to display 'Invalid Word' in red
        wordscore = 'Invalid Word'
        anscol = 'red'

    #ignore the previous statments if there was no text entered
    if len(word) == 0:
        wordscore = ''

    #make a new letter seqence
    if val == True:
        getlets()

    #display defined variables
    label4['fg'] = anscol
    label4['text'] = wordscore


#function to make all user input upercase
def allcaps(*keypress):
    var.set(var.get().upper())


#define the game timer
def timer(clock):
    
    #display time
    label1['text'] = clock
    
    #do the following until the clock runs out
    if clock > 0:
        root.after(1000, timer, clock - 1)
        
    #end the game when the time runs out
    else:
        gameover()


#ending sequence for when the time runs out
def gameover():
    
    #close main window
    root.withdraw()
    
    #display game over window
    final.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))
    final.deiconify()
    final.lift()
    ity = 'You scored ' + str(total) + ' points!'
    score['text'] = ity


#function to quit the program
def quitter():
    final.destroy()
    root.destroy()
    sys.exit()


#function for play again button
def onesmore():
    
    #reinitialize variables
    global total, clock, wordscore, anscol
    final.withdraw()
    root.deiconify()
    total = 0
    wordscore = ''
    anscol = 'blue'
    label4['fg'] = 'blue'
    root.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))

    #play again
    play()
    

#make the score at the bottom dissapear after one second
def leave():
    root.after(1000, breaker)


#part of the leave function   
def breaker():
    label4['fg'] = 'blue'

    

#make the game window    
root = Tk()
var = StringVar()

#make the game over winidow
final = Toplevel()
final.geometry('0x0+-100+-100')

#resize game window
rootwidth = 800
rootheight = 500

#place window in the middle of the user's screen
rootposx = (root.winfo_screenwidth() - rootwidth) // 2
rootposy = (root.winfo_screenheight() - rootheight) // 2 - 20
root.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))

#change root title and color
root.title('Word Scramble')
root['bg'] = 'blue'


#fuctions that I use for positioning labels and buttons
def spacery(amount):

    #create a blank label to take up vertical space
    Label(root, text = ' ', font = 'Times {}'.format(str(amount)),bg = 'blue').pack()


def spacerx(amount,way):

    #create a blank label to take up horizontal space
    that = ' '*amount
    Label(root, text = '{}'.format(that) , font = 'Times 12',bg = 'blue').pack(side = way)



#designing main game window
    
spacery(3)

#place label
label1 = Label(root, text = '', bg = 'red', font = ('Courier New', 25, 'bold'))
label1.pack(ipadx = 10)

spacery(1)

#place label
label2 = Label(root, text = 'Make any word out of the scramble (longer is better!)', bg = 'blue', fg = 'white', font = ('Comic Sans MS', 16, 'bold'))
label2.pack()

spacery(15)

#place label
label3 = Label(root, text = 'SCRAMBLE', bg = 'lightblue', font = 'Times 80')
label3.pack(ipadx = 20)

spacery(15)

#place entry box
guess = Entry(root, font = 'Times 45', justify = 'center', textvariable = var)
guess.pack(ipady = 5)

spacerx(20,'left')

#place Skip button
button1 = Button(root, text = 'Skip', font = ('Comic Sans MS', 25), bg = 'black', fg = 'white', command = getlets)
button1.pack(side = 'left', ipadx = 20)

spacerx(20,'right')

#place Submit button
button2 = Button(root, text = 'Submit', font = ('Comic Sans MS', 25), bg = 'black', fg = 'white', command = check)
button2.pack(side = 'right')

spacery(18)

#place label
label4 = Label(root, font = ('Comic Sans MS', 28, 'bold'), bg = 'blue')
label4.pack()

#resizegameover window
final.title('Game Over')

#resize and change color of game over window
final.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))
final['bg'] = '#cc3399'

#using empty label for spacing
Label(final, text = ' ', font = 'Times {}'.format(str(20)),bg = '#cc3399').pack()

#place label
sb = Label(final, text = "Time's up!", font = ('Comic Sans MS', 40, 'bold'), bg = '#cc3399')
sb.pack()

#make phrase to display
ity = 'You scored ' + str(total) + ' points!'

#using empty label for spacing
Label(final, text = ' ', font = 'Times {}'.format(str(30)),bg = '#cc3399').pack()

#place label
score = Label(final, text = ity, fg = 'white', font = ('Comic Sans MS', 52, 'bold'), bg = '#cc3399')
score.pack()

#using empty label for spacing
Label(final, text = ' ', font = 'Times {}'.format(str(27)),bg = '#cc3399').pack()

#using empty label for spacing
Label(final, text = ' ', font = 'Times {}'.format(str(250)),bg = '#cc3399').pack(side = 'left')

#place Quit button
die = Button(final, text = 'Quit', fg = 'red', bg = 'grey', font = ('Comic Sans MS', 30, 'bold'), command = quitter)
die.pack(side = 'left',ipadx = 50)

#using empty label for spacing
Label(final, text = ' ', font = 'Times {}'.format(str(250)),bg = '#cc3399').pack(side = 'right')

#place Play Again button
again = Button(final, text = 'Play Again', fg = 'red', bg = 'grey', font = ('Comic Sans MS', 30, 'bold'), command = onesmore)
again.pack(side = 'right')

#hide gameover window
final.withdraw()

#binding enter key to Submit button
root.bind('<Return>', check)


#variable and trace function to make user input all caps
var.trace('w', allcaps)



#function to begin the game
def play():

    #close title page if it's open
    insty.withdraw()
    tp.withdraw()
    root.deiconify()

    #start the chain reaction to begin the game
    getlets()
    
    #start the program with the cursor on the entry box
    guess.focus()
    
    #set timer to 60 seconds
    timer(60)


root.withdraw()


#function to make instructions appear
def viewinst():
    tp.withdraw()
    insty.deiconify()


#create title window
tp = Toplevel()

#change title page name
tp.title('Welcome')

#resize title page window
tp.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))

#change title page color
tp['bg'] = 'orange'

#place label
dm = Label(tp, text = 'DOWR\nMARSCLEB', font = ('Comic Sans MS', 80, 'bold'), bg = 'orange')
dm.pack()

#place label
cred = Label(tp, text = 'Made By James Currier', font = ('Times', 25), bg = 'orange')
cred.pack()

#using empty label for spacing
Label(tp, text = ' ', font = 'Times {}'.format(str(5)),bg = 'orange').pack()

#using empty label for spacing
Label(tp, text = ' ', font = 'Times {}'.format(str(200)),bg = 'orange').pack(side = 'left')

#place 'Instructions' button
instruct = Button(tp, text = 'Instructions', fg = 'white', bg = 'blue', font = ('Comic Sans MS', 30, 'bold'), command = viewinst)
instruct.pack(side = 'left')

#using empty label for spacing
Label(tp, text = ' ', font = 'Times {}'.format(str(200)),bg = 'orange').pack(side = 'right')

#place 'Play' button
beg = Button(tp, text = 'Play!', fg = 'white', bg = 'blue', font = ('Comic Sans MS', 30, 'bold'), command = play)
beg.pack(side = 'right',ipadx = 72)


#create instructions window
insty = Toplevel()

#rename window
insty.title('Instructions')

#resize window
insty.geometry('{width}x{height}+{x}+{y}'.format(width = rootwidth, height = rootheight, x = rootposx, y = rootposy))

#change window color
insty['bg'] = 'pink'

#using empty label for spacing
Label(insty, text = ' ', font = 'Times {}'.format(str(5)),bg = 'pink').pack()

#place label
htp = Label(insty, text = 'How To Play', font = ('Comic Sans MS', 45, 'bold'), bg = 'pink')
htp.pack()

#using empty label for spacing
Label(insty, text = ' ', font = 'Times {}'.format(str(10)),bg = 'pink').pack()

#place label
btex ="""Look at the the letters in the light blue box.
Try to make a word with any or all these letters.
Any length will be accepted, but higher words score better.
Once you have found a word, type it into the white box.
Press 'Submit' to check your word.
If your word is valid, it will be added to your total.
You can also press the 'Skip' button to change letters.
Try to get as many points as you can before time runs out."""
boom = Label(insty, text = btex, font = ('Comic Sans MS', 15, 'bold'), bg = 'pink')
boom.pack()

#using empty label for spacing
Label(insty, text = ' ', font = 'Times {}'.format(str(15)),bg = 'pink').pack()

#place 'Play!' button
gofin = Button(insty, text = 'Play!', fg = 'orange', bg = 'black', font = ('Comic Sans MS', 30, 'bold'), command = play)
gofin.pack(ipadx = 100)

#hide instructions on startup
insty.withdraw()


#keep windows open until closed by user
root.mainloop()
