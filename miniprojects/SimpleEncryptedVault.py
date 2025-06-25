# writing a simple python code using oops concept for understand encryption using encapsulation
class Vault:
    def __init__(self):
        self.password = "pythonCode"
        self.message = {"shanky":"hey there shanky its been a while now","kallu":"yo long time no see huh","shit":"hey shit how its goin ha"}
    def verification(self,index,passkey):
        if self.password != passkey:
            print("hey wrong password")
        else:
            if index == "shanky":
                print(self.message["shanky"])
            elif index == "kallu":
                print(self.message["kallu"])
            elif index == "shit":
                print(self.message["shit"])
            else:
                print(f"soory {index} theres no message for you")
if __name__=="__main__":
    obj = Vault()
    inp_index = input("enter your name: ")
    inp_passkey = input("enter the password: ")
    obj.verification(inp_index,inp_passkey)