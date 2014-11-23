import ctypes
import time
from tkinter import *
iqi=False
#TODO LIST:
#pane recolute käyttöön tekemällä ennenhiiren siirtoja
#x,y=recolute(hiirenx näytölläsi(numero),hiiren y näytölläsi(numero),näyttösix(numero,näyttösiy(numero)
#siis käytetään jaakon näytön kokoa ja koordinaatteja jaakon näytöllä
#ja tallennetaan ne x ja y nimisiin muuttujiin
#sitten ctypes windll set cursorpositioneihin laitetaan sulkuihin x , y parametreiksi
#pitäis toimia nyt kaikilla näytöillä
#sama ennen kaikkia hiiren siirtoja


def kerää3():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(840,515)
    time.sleep(1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(230,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(840,530)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(840,515)
    time.sleep(1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(430,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(840,530)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(840,515)
    time.sleep(1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(60,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    päällä()
    time10min()
    return

def kerää1():
    #ihan ylhäällä TODO lista
    
    x,y=recolute(1278,277,1920,1080)
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    x,y=recolute(1104,667,1920,1080)
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    x,y=recolute(1135,645,1920,1080)
    ctypes.windll.user32.SetCursorPos(x,y) #8
    time.sleep(1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    alkaa1()
    return
    
    
    
    
    

def time10min(numero):
    if numero == 1:
        qrq=ikkuna.after(600000,kerää1)
    else:
        qrq=ikkuna.after(600000,kerää3)
    return

def recolute(x,y,screenx,screeny):
    newx=screenx/x
    newy=screeny/y
    newsx=ctypes.windll.user32.GetSystemMetrics(0)/newx
    newsy=ctypes.windll.user32.GetSystemMetrics(1)/newy
    if newsy or newsx == float:
        newsy=round(newsy)
        newsx=round(newsx)
    else:
        pass
            
    return newsx,newsy

def alkaa1():
    
    x,y=recolute(1150,560,1920,1080)
    
    ctypes.windll.user32.SetCursorPos(x,y) #860, 400
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    x,y=recolute(1104,667,1920,1080)
    ctypes.windll.user32.SetCursorPos(x,y) #840, 530
    time10min(1)
    return

def alkaa3():
    s=0
    ctypes.windll.user32.SetCursorPos(1150, 560)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(230,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1150, 560)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(430,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1150, 560)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(60,20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1104,667)
    
    #ihan ylhäällä todo lista
    
    time10min(3)
    return

#ihan ylhäällä todo lista
ikkuna = Tk()
ikkuna.title("ggeb")
ikkuna.geometry("250x150")
nappi1=Button(ikkuna,text="kerää veroja 1.p",command=alkaa1)
nappi2=Button(ikkuna,text="kerää veroja 3.p",command=alkaa3)
nappi1.pack(side=LEFT)
nappi2.pack(side=LEFT)
ikkuna.mainloop()
    


    
