def alkaa1():
    s=0
    ctypes.windll.user32.SetCursorPos(1150, 560) #860, 400
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)
    ctypes.windll.user32.SetCursorPos(1104,667) #840, 530
    while s<=10:
        time.sleep(1)
        s+=1
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
    
    while s<=598:
        time.sleep(1)
        s+=1
        continue
    
    
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
    alkaa3()
    return


    

def __main__():
    
    ikkuna = Tk()
    ikkuna.title("ggeb")
    ikkuna.geometry("250x150")
    nappi1=Button(ikkuna,text="kerää veroja 1.p",command=alkaa1)
    nappi2=Button(ikkuna,text="kerää veroja 3.p",command=alkaa3)
    nappi1.pack(side=LEFT)
    nappi2.pack(side=LEFT)
    ikkuna.mainloop()
if __name__ == "__main__":
    import ctypes
    import time
    from tkinter import *
    __main__()
