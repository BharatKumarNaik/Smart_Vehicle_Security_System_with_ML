from tkinter import *
from PIL import Image,ImageTk
import socket
import time
from threading import *
device1 = Tk()
device1.title("Thief 1")
width = 200
height = 200
device1.geometry(str(width)+"x"+str(height)+"+950+200")
device1.resizable(False, False)
background = Canvas(width = width, height = height, highlightthickness=0, bg = 'white')
background.pack(expand = YES, fill = BOTH)
background_image = "device1.png"
image = Image.open(background_image)
image = image.resize((width,height), Image.ANTIALIAS)
cover = ImageTk.PhotoImage(image)
background.create_image(0, 0, image = cover, anchor = NW)
dist = 'None'
def send():
    global dist
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1",8082))
    clientSocket.send(str(dist).encode())
def capture():
    global dist
    (clientConnected, clientAddress) = serverSocket.accept()
    dataFromClient = clientConnected.recv(2048)
    dist = dataFromClient.decode()
    clientConnected.close()
    signalBar['text']='Connected'
    loc_key_fob = dist.split(':')[0]
    displayBar['text']='Loc: '+loc_key_fob
    t2 = Thread(target=capture)
    time.sleep(5)
    t2.start()
port_file = open("conn_to.txt", "w")
port_file.write('8081')
port_file.close()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1',8081))
serverSocket.listen(5)
send=Button(device1,relief=RAISED,command=send,text = 'I', font='Calibri 10 bold',compound="center",bg = '#00ab41',width=2, height=1)
send.place(x=89,y=170)
signalBar = Label(device1,relief=FLAT,text = 'Not connected', font='Consolas 7 bold',bg = '#006730', width=37, height=1, anchor = 'e')
signalBar.place(x=5,y=2)
displayBar = Label(device1,relief=FLAT,text = 'N/A', font='Consolas 15 bold',bg = '#006730', width=17, height=1, anchor = 'center')
displayBar.place(x=3,y=18.25)
DummyBar = Label(device1,relief=FLAT,text = '',bg = '#006730', width=2, height=1, anchor = 'e')
DummyBar.place(x=3,y=2)
t1=Thread(target=capture)
t1.start()
device1.mainloop()