#importing GUI interface module====>>>

import tkinter.messagebox
from tkinter import*

#rooting module=====>>>

root =Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background ='Cadet Blue')

#Frames of the game===========>>>

Tops = Frame(root, bg ='Cadet Blue', pady =2, width =1350, height=100, relief =RIDGE)
Tops.grid(row=0, column=0)

lblTitle =Label(Tops, font=('arial',50,'bold'), text ="Tic Tac Toe", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root, bg='Powder Blue', bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame2.grid(row=1,column=0)

# making players variables=====>>>

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True

#logic=====>>>

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        ScoreKeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        ScoreKeeper()
        
        
#PlayerX winning logic=====>>>

        
def ScoreKeeper():
    
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background = 'powder blue')
        button2.configure(background = 'powder blue')
        button3.configure(background = 'powder blue')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")

    if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background = 'red')
        button5.configure(background = 'red')
        button6.configure(background = 'red')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")
   
    if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background = 'Cadet blue')
        button8.configure(background = 'Cadet blue')
        button9.configure(background = 'Cadet blue')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")
 
    if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background = 'yellow')
        button4.configure(background = 'yellow')
        button7.configure(background = 'yellow')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")

    if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background = 'pink')
        button5.configure(background = 'pink')
        button8.configure(background = 'pink')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")
  
    if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background = 'Cadet blue')
        button6.configure(background = 'Cadet blue')
        button9.configure(background = 'Cadet blue')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")
   
    if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background = 'red')
        button5.configure(background = 'red')
        button9.configure(background = 'red')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")

    if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background = 'Cadet blue')
        button5.configure(background = 'Cadet blue')
        button7.configure(background = 'Cadet blue')
        n =float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerX won a game")


#PlayerO winning logic=====>>>

        
    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background = 'orange')
        button2.configure(background = 'orange')
        button3.configure(background = 'orange')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")

    if (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background = 'blue')
        button5.configure(background = 'blue')
        button6.configure(background = 'blue')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")

    if (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background = 'green')
        button8.configure(background = 'green')
        button9.configure(background = 'green')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")
    
    if (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background = 'yellow')
        button4.configure(background = 'yellow')
        button7.configure(background = 'yellow')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")
   
    if (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background = 'pink')
        button5.configure(background = 'pink')
        button8.configure(background = 'pink')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")

    if (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background = 'Cadet blue')
        button6.configure(background = 'Cadet blue')
        button9.configure(background = 'Cadet blue')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")
   
    if (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background = 'orange')
        button5.configure(background = 'orange')
        button9.configure(background = 'orange')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")
    
    if (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background = 'Cadet blue')
        button5.configure(background = 'Cadet blue')
        button7.configure(background = 'Cadet blue')
        n =float(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner Winner Chicken Dinner", "PlayerO won a game")
   
def Reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " " 

    button1.configure(background = 'gainsboro')
    button2.configure(background = 'gainsboro')
    button3.configure(background = 'gainsboro')
    button4.configure(background = 'gainsboro')
    button5.configure(background = 'gainsboro')
    button6.configure(background = 'gainsboro')
    button7.configure(background = 'gainsboro')
    button8.configure(background = 'gainsboro')
    button9.configure(background = 'gainsboro')

def NewGame():
    Reset()
    PlayerX.set(0)
    PlayerO.set(0)




lblPlayerX =Label(RightFrame1, font=('arial',40,'bold'), text ="Player X:", padx=2, pady=2, bg='Cadet Blue')
lblPlayerX.grid(row=0,column=0,sticky=W)
txtPlayerX =Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg='black',
                  textvariable=PlayerX, width=10, justify=LEFT).grid(row=0,column=1)

lblPlayerO =Label(RightFrame1, font=('arial',40,'bold'), text ="Player O:", padx=2, pady=2, bg='Cadet Blue')
lblPlayerO.grid(row=1,column=0,sticky=W)
txtPlayerO =Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg='black',
                  textvariable=PlayerO, width=10, justify=LEFT).grid(row=1,column=1)

#buttons to reset and newgame================>>>
btnReset = Button(RightFrame2, text="Reset", font=('Times 26 bold'),
                  height=3, width=20, bg='gainsboro', command=Reset)
btnReset.grid(row=0, column=0, pady=11, padx=6)

btnNewGame = Button(RightFrame2, text="New Game", font=('Times 26 bold'),
                    height=3, width=20, bg='gainsboro', command=NewGame)
btnNewGame.grid(row=1, column=0, pady=10, padx=6)


#buttons to play===============>>>
button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)


root.mainloop()
