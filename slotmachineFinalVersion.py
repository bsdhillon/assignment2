#Source File Name: slotmachine.py
#Author's Name: Balwinder Dhillon
#Date last modified: June 8, 2013
#Last Modified By: Balwinder Dhillon

#import tkinter
from Tkinter import *
import tkMessageBox
import random
class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        ### Our topmost frame is called myContainer1
        self.myContainer1 = Frame(parent, bg="blue") 
        self.myContainer1.pack()
        #------ constants for controlling layout ------
        button_width = 15
        self.jackpotVal = 500 
        self.money = 1000

        ### Inside myContainer1, first we create buttons_frame.
        ### Then we create top_frame and bottom_frame.
        ### These will be our demonstration frames.
        # buttons frame
        self.buttons_frame = Frame(self.myContainer1) 
        self.buttons_frame.pack(
        side=TOP, fill=BOTH,
        expand=YES,)

        self.top_frame = Frame(self.myContainer1)
        self.top_frame.pack(side=TOP,
        fill=BOTH,
        expand=YES,
        ) 
        # bottom frame
        self.bottom_frame = Frame(self.myContainer1,
        borderwidth=5, relief=RIDGE,
        height=50,
        ) 
        self.bottom_frame.pack(side=TOP,
        fill=BOTH,
        expand=YES,
        ) 
        #last frame at bottom
        self.last_frame = Frame(self.myContainer1, borderwidth=5, relief=RIDGE, height=50)
        self.last_frame.pack(side=TOP,
        fill=BOTH,
        expand=YES,
        )
        self.images = list()
        self.images.append(PhotoImage(file="images/1.gif"))
        self.images.append(PhotoImage(file="images/2.gif"))
        self.images.append(PhotoImage(file="images/3.gif"))
        self.images.append(PhotoImage(file="images/4.gif"))
        self.images.append(PhotoImage(file="images/5.gif"))
        self.images.append(PhotoImage(file="images/6.gif"))
        self.images.append(PhotoImage(file="images/7.gif"))
        self.images.append(PhotoImage(file="images/8.gif"))
        ### Now we will put three buttons in the top frame,
        ### orientation within top_frame.
        self.image = PhotoImage(file="images/8.gif")
        self.button4 = Button(self.top_frame, command=self.buttonspinClick, image=self.image)
        self.button4.configure(text="")
        self.button4.focus_force()
        self.button4.configure(
            width=150, 
            height=150,
            borderwidth=5, relief=RIDGE,
            )
        self.button4.pack(side=LEFT)
        self.button4.bind("<Return>", self.buttonspinClick_a)
        
        #setting the default image on the button
        self.button5 = Button(self.top_frame, command=self.buttonspinClick, image=self.image)
        self.button5.configure(text="", )
        self.button5.focus_force()
        self.button5.configure(
            width=150, 
            height=150,
            borderwidth=5, relief=RIDGE,
            )
        self.button5.pack(side=LEFT)
        self.button5.bind("<Return>", self.buttonspinClick_a)
        #self.image = PhotoImage(file="Sonic-Animated.gif")
        self.button6 = Button(self.top_frame, command=self.buttonspinClick, image=self.image)
        self.button6.configure(text="")
        self.button6.focus_force()
        self.button6.configure(
            width=150, 
            height=150,
            borderwidth=5, relief=RIDGE,
            )
        self.button6.pack(side=LEFT)
        self.button6.bind("<Return>", self.buttonspinClick_a)
        
        # now we add the buttons to the buttons_frame
        #creating the spin button
        self.buttonspin = Button(self.buttons_frame, command=self.buttonspinClick)
        self.buttonspin.configure(text="Spin", background= "green")
        self.buttonspin.focus_force()
        self.buttonspin.configure(
            width=button_width, 
            borderwidth=5, relief=RIDGE,
            #pady=button_pady 
            )
        self.buttonspin.pack(side=LEFT)
        self.buttonspin.bind("<Return>", self.buttonspinClick_a)
        #exit button
        self.buttonexit = Button(self.buttons_frame, command=self.buttonexitClick_a)
        self.buttonexit.configure(text="Cancel", background="red")
        self.buttonexit.configure(
        width=button_width,
        borderwidth=5, relief=RIDGE, 
        )
        self.buttonexit.pack(side=LEFT)
        self.buttonexit.bind("<Return>", self.buttonexitClick_a)
        # Reset button
        self.buttonreset = Button(self.buttons_frame, command=self.buttonresetClick_a)
        self.buttonreset.configure(text="Reset", background= "green")
        self.buttonreset.focus_force()
        self.buttonreset.configure(
            width=button_width, 
            borderwidth=5, relief=RIDGE,
            )
        self.buttonreset.pack(side=RIGHT)
        self.buttonreset.bind("<Return>", self.buttonresetClick_a)
        #labels for jackpot and balance in the bottom frame
        self.labeljack = Label(self.bottom_frame, fg="red", font=("Helvetica", 16))
        self.labeljack["text"] = "Jackpot: " + str(self.jackpotVal)
        self.labeljack.pack(side=LEFT)
        
        self.labelmoney = Label(self.bottom_frame,  fg="red", font=("Helvetica", 16))
        self.labelmoney["text"] = "Money: " + str(self.money)
        self.labelmoney.pack(side=RIGHT)
        
        
        self.label3 = Label(self.last_frame, text="Your Bet", fg="red", font=("Helvetica", 16))
        self.label3.pack(side=LEFT)
        #creating text box for bet amount
        self.entrybet = Entry(self.last_frame, font=("Helvetica", 16), width="11")
        self.entrybet.pack(side=LEFT)
        #s = self.entrybet.get()
    
    def jckEntryUpdate(self,jackobj,currVal):
        jackobj.insert(INSERT, str(currVal))
        jackobj.configure(state="disabled", borderwidth=3)
        jackobj.pack(side=LEFT)
    #handling the click event of spin button
    def buttonspinClick(self):
        #if self.buttonspin["background"] == "green":
            #self.buttonspin["background"] = "yellow"
            #check if user has the balance to play
        if self.money < 0:
            tkMessageBox.showerror(" Invalid Input", "You Have no money left ") 
        s = self.entrybet.get()
        temp = int(s)  
        #check if bet amount is greater than zero and less than total money user has
        if temp > 1000 or temp <= 0 :
            tkMessageBox.showerror(" Invalid Input", "You have only $1000 to place a bet. No negative input accepted")
                   
        else:
            #loading images randomly on the butons
            #jack = int(self.entryjack.get())
            self.money -= temp
            jackMoney = (self.jackpotVal + (temp * 3))
            self.labeljack["text"] = "Jackpot: " + str(jackMoney)
            self.labelmoney["text"] = "Money: " + str(self.money)
            img1 = self.getRandomNumber()
            self.button4.configure(image=self.images[img1])
            img2 = self.getRandomNumber()
            self.button5.configure(image=self.images[img2])
            img3 = self.getRandomNumber()
            self.button6.configure(image=self.images[img3])
            if img1==img2 and img1==img3:
                self.money = self.jackpotVal + (3 * temp)
                self.lblmoney["text"] = "Money : " +str(self.money)
                #self.lbljack["text"] = "Jackpot : " + str(self.jackpotVal)
            elif img1==img2 or img2==img3 or img1==img3:
                self.money += temp*2
                self.lblmoney["text"] = "Money : " +str(self.money)
                #self.lbljack["text"]="Jackpot : " +str(self.jackpotVal)
    #handling exit button
    def buttonexitClick_a(self):
        self.myParent.destroy()
    def buttonspinClick_a(self, event):
        self.buttonspinClick()
    #handling reset button
    def buttonresetClick_a(self):
        self.labelmoney["text"]="Money: 1000"
        self.labeljack["text"]="Jackpot: 500"
        self.entrybet.insert(0,"")
        self.button4.configure(image=self.image)
        self.button5.configure(image=self.image)
        self.button6.configure(image=self.image)
    #generating random number
    def getRandomNumber(self):
        return random.randrange(1,8,1)
def main():
    root = Tk()
    myapp = MyApp(root)
    root.geometry("600x400+200+200")

    root.mainloop()

if __name__ == "__main__": main()