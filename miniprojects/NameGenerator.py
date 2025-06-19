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
    window.geometry("1000x500")
    window.config(background="#1C2526")

    label1 = Label(window,
                   bg="#192A54",
                   fg="#39FF14",
                   font=("Impact", 40),
                   text="TROLLING FRIENDS IS PURE FUN!!")
    entry = Entry(window,
                  font=("Comic Sans MS",40),
                  fg="#FFFFFF",
                  bg="#000000")
    

    label = Label(window,
                  font=("Comic Sans MS",40),
                  bg="#1C2526",
                  fg="#39FF14")

    trolls_list = [' baka',' pervy sage',' damn you',' mudhead','-chan']
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

    button = Button(window,text="submit",
                    command=show_input,
                    font=("Comic Sans MS",27),
                    bg="#2F4F4F",
                    fg="#FFFF00",
                    activebackground="#FF0090")


    label1.pack()
    entry.pack(anchor="w")
    button.pack(anchor="w")
    label.pack(anchor="center")
    window.mainloop()
      
        

    