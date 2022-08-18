import os
from time import sleep

# This file's name is tricks.py
def loading_function(n: int):
    isInt = isinstance(n, int)
    
    if(isInt == False):
        raise 'You have to input an int type value!'
        
    print("Loading" + '.'*(n))
    sleep(1)
    os.system('clear')
    
while True:
    loading_function(1)
    loading_function(2)
    loading_function(3)
    loading_function(4)

'''
import tricks

while True:
    tricks.loading_function(1)
'''
