from tkinter import *
from PIL import Image,ImageTk
import socket
import time
from threading import *
keyfob = Tk()
keyfob.title("Key Fob")
width = 200
height = 200
keyfob.geometry(str(width)+"x"+str(height)+"+950+0")
keyfob.resizable(False, False)
background = Canvas(width = width, height = height, highlightthickness=0, bg = 'white')
background.pack(expand = YES, fill = BOTH)
background_image = "key_fob.png"
image = Image.open(background_image)
image = image.resize((width,height), Image.ANTIALIAS)
cover = ImageTk.PhotoImage(image)
background.create_image(0, 0, image = cover, anchor = NW)
def direct():
    port_file = open("conn_to.txt", "r")
    port = int(port_file.read())
    x = keyfob.winfo_x()
    y = keyfob.winfo_y()
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1",port))
    clientSocket.send((str((x,y))+':(-150,700)').encode())
    t2 = Thread(target=direct)
    time.sleep(5)
    t2.start()
t1=Thread(target=direct)
t1.start()
keyfob.mainloop()