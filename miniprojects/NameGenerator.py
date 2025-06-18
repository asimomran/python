# for this project when i give name of a certain person i should get the output as new name with a troll at the last
# first i will create class which will have all the works done 
# then i will create a list probably inside the class itself
# i will then return or print the name with a random troll at the last of the name
import random
from tkinter import *
class troll:
    def random_troll_name(self,name):
        self.name = name
        random_troll = random.choice(trolls_list)
        new_name = self.name + random_troll
        return new_name

if __name__=="__main__":
     
    window = Tk()
    window.title("This is a fun game")

    entry = Entry(window)

    label = Label(window)
    
    trolls_list = ['baka','pervy sage','damn you','mudhead','-chan']
    def show_input():
        name = entry.get()
        if name=="":
            label.config(text="invalid bro")
        elif name=="exit": 
            window.quit()
        else:    
            obj = troll()
            final_name = obj.random_troll_name(name)
            label.config(text=final_name)

    button = Button(window,text="submit",command=show_input)
    entry.pack()
    button.pack()
    label.pack()
    window.mainloop()
      
        

    