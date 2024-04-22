def func():

    class Account():
        
        def __init__(self,user=input("Decime tu nombre: ")):
            
            self.user = user
            
        
        def initialize(self):
            
            x = " "
            
            allowed1 = True
            
            allowed2 = True
            
            database = {"jose":"josesito123","joaquin":"joaquinsito123","Pedro":"Pedrito123"}
            
            if self.user in database:
                
                print(f"Welcome {self.user}")
                
                x = input("Please enter your password: ")
                
                if x in database[self.user]:
                    
                    print("Welcome, you can continue now")
                    
                    return True
                
                else:
                    allowed2 = False
                    
                    return allowed2
                
            else:
                allowed1 = False
                
                return allowed1
            
        
    instance = Account()
    
    ask = " "
    
    while ask not in "stop":
        
        y = instance.initialize()
        
        if y == True:
            
            pass
        else:
            
            print("Permission denied")
            
            break
        
        ask = input("What do you want to do: ")
        
func()
            
            