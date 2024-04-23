#webbrowser

import webbrowser as wb

def func():
    
    class Class():
        
        def __init_(self):
            pass
        
        def define_search(self):
            
            srch = input("que queres buscar: ")
            
            wb.open(f"https://www.google.com/search?q={srch}+&oq={srch}+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQLhhA0gEIMjg3OWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8")
            
            print("Page opened")
    
    instance = Class()
    
    ask = " "
    
    while ask not in "no":
        
        instance.define_search()
        ask = input("Do you want to continue searching: ")

func()