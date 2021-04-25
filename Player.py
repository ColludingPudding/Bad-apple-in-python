import os
import time
import pickle
import tkinter
import threading
from playsound import playsound

path = "C:/Users/Dell/Desktop/Bad-apple-in-python-master"                        
with open(path + '/0.dat', 'rb') as fp:
    strings = pickle.load(fp)                                                                          

window = tkinter.Tk()                                                                                   
window.title('Bad Apple') 
window.geometry('300x220') 
player = tkinter.Label(window, font=('Courier', 4))                           
player.place(x = 0,y = 0)  
playsound(path + '/badapple.mp3', False)

count = 1                                                                    
time.sleep(3)
start_t = time.time()
for each in strings:
    t = 1/30 * count - time.time() + start_t # some Chinese magic bullshit to sync it perfectly to 30 fps                                                  
    if t>0:                                                                                            
        time.sleep(t)
    player['text'] = each
    window.update()
    count += 1
window.mainloop()