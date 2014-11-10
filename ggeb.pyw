import ctypes
import time
from tkinter import *
#TODO LIST:
#pane recolute käyttöön tekemällä ennenhiiren siirtoja
#x,y=recolute(hiirenx näytölläsi(numero),hiiren y näytölläsi(numero),näyttösix(numero,näyttösiy(numero)
#siis käytetään jaakon näytön kokoa ja koordinaatteja jaakon näytöllä
#ja tallennetaan ne x ja y nimisiin muuttujiin
#sitten ctypes windll set cursorpositioneihin laitetaan sulkuihin x , y parametreiksi
#pitäis toimia nyt kaikilla näytöillä
#sama ennen kaikkia hiiren siirtoja
def stopperi():
    pass

def päällä():
    nappi1.Destroy()
    nappi2.Destroy()
    stopnappi=Button(ikkuna,Label="stop",command = stopperi)
    stopnappi.pack()
    return

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

def kerää1():
    #ihan ylhäällä TODO lista
    ctypes.windll.user32.SetCursorPos(1278,277)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1104,667)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1135,645) #8
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
    s=0
    ctypes.windll.user32.SetCursorPos(1150, 560) #860, 400
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1104,667) #840, 530
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
    


    
