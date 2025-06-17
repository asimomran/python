# for this project when i give name of a certain person i should get the output as new name with a troll at the last
# first i will create class which will have all the works done 
# then i will create a list probably inside the class itself
# i will then return or print the name with a random troll at the last of the name
import random
import time
from tkinter import *

window = Tk()
window.geometry("1000x500")
window.title("A Little Game")
entry = Entry(window)

label = Label(window,text="TROLLING FRIENDS IS PURE FUN")
label.config(background="black",foreground="darkblue")
button = Button(window,text="confirm?")
class troll:
    def __init__(self,name):
        print("processing.....")
        self.name = name
    
    def random_troll_name(self):
        random_troll = random.choice(trolls_list)
        time.sleep(3)
        print(f"{self.name} {random_troll}")

if __name__=="__main__":
    trolls_list = ['baka','pervy sage','damn you','mudhead','-chan']
    while True:         
        name = input("enter your friend's name: (write exit to exit)")
        if name=="":
            print("invalid bro")
            break
        elif name == "exit":
            break
        else:    
            obj = troll(name)
            obj.random_troll_name()
            
entry.pack()
button.pack()
label.pack()
window.mainloop()
