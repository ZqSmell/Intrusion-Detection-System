import os
import cv2
import time
import socket
import platform
from tkinter import *
import tkinter.messagebox
from pushbullet import PushBullet


#check for internet connectivity
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False   

#takes intruder pic
def intruder_pic():
    cam=cv2.VideoCapture(0)
    s,im=cam.read() 
    cv2.imwrite("Intruder.bmp",im)
         
#pushes captured image to Mobile
def Image_send(pb):
    with open("Intruder.bmp", "rb") as pic:
        file_data = pb.upload_file(pic, "Intruder.bmp")

    push = pb.push_file(**file_data)
        
#log off PC if Intruder Suspected
def logOff():
    opsys = platform.system()
    if opsys == 'Windows':
        import ctypes
        ctypes.windll.user32.LockWorkStation()
    else:
        os.popen('gnome-screensaver-command --lock')        



def start(api_key,root):
    # flag used to count number of attempt left
    flag = 10
    while 1:
        if is_connected():
            try:
                pb =PushBullet(api_key)
            except:
                tkinter.messagebox.showinfo('Invalid Key','Entered key is invalid!')
                break
            pushMsg =pb.push_note("PYTHON : ","Found Internet Connectivity, is this you? if not message 'No' otherwise message 'Yes' ")
            time.sleep(30)
            val = pb.get_pushes()
            action = val[0]['body']
            print(action)
            if action.lower() == 'no':
               intruder_pic()
               Image_send(pb)
               time.sleep(10)
               logOff()
               root.destroy()
               break
            elif action.lower() == 'yes':
                flag = 10
                time.sleep(3600)
            else:
                flag -= 1
                if flag == 0:
                    intruder_pic()
                    Image_send(pb)
                    time.sleep(10)
                    logOff()
                    root.destroy()
                    break
                time.sleep(60)    
        else:
            time.sleep(600)


#gui using tkinter
root = Tk()
root.title("Intrusion Detection System")
root.minsize(400,300)
root.maxsize(400,300)
root.configure(background='black')

L0 = Label(root, text="Intrusion Detection System", fg = "white", bg = "black", font=("Times", 18)) 
L0.place(x=195, y=45, anchor="center")

L1 = Label(root, text="Enter Your PushBullet ApiKey: ", fg = "white", bg = "black", font=("Helvetica", 10))
L1.place(x=205, y=135, anchor="center")

E1 = Entry(root, bd =2)
E1.place(x=205, y=165, anchor="center")

B = Button(root, bd =3, text ="Submit", fg = "white", bg = "black", command= lambda: start(E1.get(),root))
B.place(x=205, y=195, anchor="center")

root.mainloop()


