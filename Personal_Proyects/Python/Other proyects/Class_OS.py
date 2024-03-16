import os
import collections


class Computer_info():
    def __init__(self):
        pass
    
    def __str__(self):
        return "This is the computer info class"
    
    def file_counter(self):
        for folder,sub,file in os.walk("C:\\Users\\Luca\\Desktop\\Personal"):
            for fol in folder:
                collections.Counter(fol)
            
            for s in sub:
                collections.Counter(s)
            
            for fil in file:
                collections.Counter(fil)
                
                
CI_instance = Computer_info()

CI_instance.file_counter()