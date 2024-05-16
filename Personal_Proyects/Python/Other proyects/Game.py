from abc import ABC, abstractclassmethod

def game():
    
    class Players(ABC):
        
        @abstractclassmethod
        
        def __init__(self,username,habilities,power=0):
            
            self.username = username
            self.habilities = habilities
            self.power = power
            
        @abstractclassmethod 
        
        def set_name(self):
            pass
        
        @abstractclassmethod
        
        def set_habilities(self):
            pass
        
        @abstractclassmethod 
        
        def set_power(self):
            pass
        
        
        
        
        
        
    class Player1(Players):
        
        def __init__(self,username,habilities,power):
            super().__init__(username, habilities,power)
            
        def set_name(self):
            
            self.username = input("Player 1 username: ")
            
        def set_habilities(self):
            
            self.habilities = []
            
            x = input("What first hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
            
            y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
            
            self.habilities.append(x)
            
            if x == "plant":
                
                if y == "fire":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "water":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
                    
            elif x == "water":
                
                if y == "plant":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "fire":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
            
            elif x == "fire":
                
                if y == "water":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "plant":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
                    
            else:
                return "You are a boludo"
            
        def set_power(self):
            
            for obj in self.habilities:
                
                if obj == "fire":
                    
                    self.power += 20
                    
                elif obj == "plant":
                    
                    self.power += 10
                
                elif obj == "water":
                    self.power += 10
                    
                    
                    
                    
        
    class Player2(Players):
            
        def __init__(self,username,habilities,power):
            super().__init__(username, habilities,power)
            
        def set_name(self):
            
            self.username = input("Player 2 username: ")
            
        def set_habilities(self):
            
            self.habilities = []
            
            x = input("What first hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
            
            y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
            
            self.habilities.append(x)
            
            if x == "plant":
                
                if y == "fire":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "water":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
                    
            elif x == "water":
                
                if y == "plant":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "fire":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
            
            elif x == "fire":
                
                if y == "water":
                    
                    print("The two habilities that you choose are not compatible, please enter again your second hability")
                    
                    y = input("What second hability do you want, water(10 power, weak against plant), fire(20 power, weak againsts water), plant(10 power, weak against fire): ")
                
                elif y == "plant":
                    self.habilities.append(y)
                    print(f"Okey, your habilities are {self.habilities}")
                    
            else:
                return "You are a boludo"
            
        def set_power(self):
            
            for obj in self.habilities:
                
                if obj == "fire":
                    
                    self.power += 20
                    
                elif obj == "plant":
                    
                    self.power += 10
                
                elif obj == "water":
                    self.power += 10
                    
                    
                    
                    
                    
                        
            
    player1 = Player1()
    
    player2 = Player2()
    
    class Fusion(Players):
        
        def __init__(self, username, habilities,power):
            
            super().__init__(self,username, habilities,power)
        
        def set_name(self):
            
            self.username = input("Enter the name of the fusion: ")
        
        def set_habilities(self):
            
            self.habilities = []
            
            self.habilities.append(player1.habilities)
            
            self.habilities.append(player2.habilities)
            
            print(f"Your habilities are {self.habilities}")
        
        def set_power(self):
            
            for obj in self.habilities:
                
                if obj == "fire":
                    
                    self.power += 20
                    
                elif obj == "plant":
                    
                    self.power += 10
                
                elif obj == "water":
                    self.power += 10
            
    fusion = Fusion()
    
    def set_players():
        
        player1.set_name()
        player1.set_habilities()
        player1.set_power()
        
        player2.set_name()
        player2.set_habilities()
        player2.set_power()
        
    #Run the players class
    set_players()

game()
    
    