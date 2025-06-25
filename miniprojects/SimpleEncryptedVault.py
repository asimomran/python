# writing a simple python code using oops concept for understand encryption using encapsulation
class Vault:
    def __init__(self):
        self.__password = "pythonCode"
        self.__messages = {"shanky":"hey there shanky its been a while now",
                           "kallu":"yo long time no see huh",
                           "shit":"hey shit how its goin ha"}
    def verification(self,index,passkey):
        if self.__password != passkey:
            print("hey wrong password")
        else:
            if self.__messages.get(index) == None:
                print("there's no message for you!")
            else:
                print(self.__messages.get(index))
            
    
if __name__=="__main__":
    obj = Vault()
    inp_index = input("enter your name: ")
    inp_passkey = input("enter the password: ")
    obj.verification(inp_index,inp_passkey)
