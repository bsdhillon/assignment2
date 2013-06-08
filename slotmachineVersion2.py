from Tkinter import *
import tkMessageBox
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
        self.last_frame = Frame(self.myContainer1, borderwidth=5, relief=RIDGE, height=50)
        self.last_frame.pack(side=TOP,
        fill=BOTH,
        expand=YES,
        )
        ### Now we will put two more frames, left_frame and right_frame,
        ### inside top_frame. We will use HORIZONTAL (left/right)
        ### orientation within top_frame.
        # left_frame
        self.image = PhotoImage(file="images/strawberry.gif")
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
        
        #self.image = PhotoImage(file="Sonic-Animated.gif")
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
        self.buttonexit = Button(self.buttons_frame, command=self.buttonexitClick)
        self.buttonexit.configure(text="Cancel", background="red")
        self.buttonexit.configure(
        width=button_width,
        borderwidth=5, relief=RIDGE, 
        #padx=button_padx, 
        #pady=button_pady 
        )
        self.buttonexit.pack(side=LEFT)
        self.buttonexit.bind("<Return>", self.buttonexitClick_a)
        self.button3 = Button(self.buttons_frame, command=self.buttonspinClick)
        self.button3.configure(text="Reset", background= "green")
        self.button3.focus_force()
        self.button3.configure(
            width=button_width, 
            borderwidth=5, relief=RIDGE,
            #padx=button_padx, 
            #pady=button_pady 
            )
        self.button3.pack(side=RIGHT)
        self.labeljack = Label(self.bottom_frame, fg="red", font=("Helvetica", 16))
        self.labeljack["text"] = "Jackpot: " + str(self.jackpotVal)
        self.labeljack.pack(side=LEFT)
        #self.entryjack = Entry(self.bottom_frame, font=("Helvetica", 16), width="12")
        #was here
        
        #self.jckEntryUpdate(self,self.entryjack,self.jackpotVal)
        #self.entryjack.configure(state="disabled", borderwidth=3)
        #self.entryjack.pack(side=LEFT)
        
        
        
        #self.entrymoney = Entry(self.bottom_frame, font=("Helvetica", 16), width="12")
        #self.entrymoney.pack(side=RIGHT)
        #self.entrymoney.insert(INSERT, "1000")
        #self.entrymoney.configure(state="disabled", borderwidth=3)
        self.labelmoney = Label(self.bottom_frame,  fg="red", font=("Helvetica", 16))
        self.labelmoney["text"] = "Money: " + str(self.money)
        self.labelmoney.pack(side=RIGHT)
        
        
        self.label3 = Label(self.last_frame, text="Your Bet", fg="red", font=("Helvetica", 16))
        self.label3.pack(side=LEFT)
        self.entrybet = Entry(self.last_frame, font=("Helvetica", 16), width="11")
        self.entrybet.pack(side=LEFT)
        #s = self.entrybet.get()
        self.entryresult = Entry(self.last_frame, width="18")
        self.entryresult.pack(side=RIGHT)
        self.entryresult.configure(state="disabled", borderwidth=3)
        self.label4 = Label(self.last_frame, text="Result", fg="red", font=("Helvetica", 16))
        self.label4.pack(side=RIGHT)
    
    def jckEntryUpdate(self,jackobj,currVal):
        jackobj.insert(INSERT, str(currVal))
        jackobj.configure(state="disabled", borderwidth=3)
        jackobj.pack(side=LEFT)
    
    def buttonspinClick(self):
        #if self.buttonspin["background"] == "green":
            #self.buttonspin["background"] = "yellow"
        s = self.entrybet.get()
        temp = int(s)  
        if temp > 1000 or temp <= 0 :
            tkMessageBox.showerror(" Invalid Input", "You have only $1000 to place a bet. No negative input accepted")
                   
        else:
            #jack = int(self.entryjack.get())
            self.money -= temp
            jackMoney = (self.jackpotVal + (temp * 3))
            self.labeljack["text"] = "Jackpot: " + str(jackMoney)
            self.labelmoney["text"] = "Money: " + str(self.money)
            #self.entryjack.insert(self,0, "867")
            #self.entryjack.pack(side=LEFT)
    def buttonexitClick(self):
        self.myParent.destroy()
    def buttonspinClick_a(self, event):
        self.buttonspinClick()
    def buttonexitClick_a(self, event):
        self.buttonexitClick()

def main():
    root = Tk()
    myapp = MyApp(root)
    root.geometry("600x400+200+200")

    root.mainloop()

if __name__ == "__main__": main()