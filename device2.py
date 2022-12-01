from tkinter import *
from PIL import Image,ImageTk
import socket
import time
from threading import *
device2 = Tk()
device2.title("Thief 2")
width = 200
height = 200
device2.geometry(str(width)+"x"+str(height)+"+950+200")
device2.resizable(False, False)
background = Canvas(width = width, height = height, highlightthickness=0, bg = 'white')
background.pack(expand = YES, fill = BOTH)
background_image = "device2.png"
image = Image.open(background_image)
image = image.resize((width,height), Image.ANTIALIAS)
cover = ImageTk.PhotoImage(image)
background.create_image(0, 0, image = cover, anchor = NW)
dist = 'None'
dev_dist = 'None'
def intrude():
    global dist, dev_dist
    x = device2.winfo_x()
    y = device2.winfo_y()
    dev_dist = str((x,y))
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("127.0.0.1",8080))
    clientSocket.send((dev_dist+':'+dist).encode())
    signalBar['text'] = 'Your location: '+str(device2.winfo_x())
    bound1 = int(dist[1:dist.index(',')])
    bound2 = int(dist[dist.index(',')+1:len(dist)-1])
    chk_dist = dist[1:dist.index(',')]
    if(x in range(bound1,bound2)):
        # Success (Unlocked)
        displayBar['text'] = '...'
    else:
        displayBar['font'] = 'Consolas 15 bold'
        displayBar['text'] = 'Range: '+dist
    t3 = Thread(target=intrude)
    time.sleep(5)
    t3.start()
def capture():
    global dist
    (clientConnected, clientAddress) = serverSocket.accept()
    dataFromClient = clientConnected.recv(2048)
    dist = dataFromClient.decode()
    clientConnected.close()
    signalBar['text'] = 'Your location: '+str(device2.winfo_x())
    dist = dist.split(':')[1]
    intrude()
    time.sleep(5)
    t2 = Thread(target=capture)
    t2.start()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1',8082))
serverSocket.listen(5)
# send=Button(device2,relief=RAISED,command=intrude,text = 'O', font='Calibri 10 bold',compound="center",bg = 'red',width=2, height=1)
# send.place(x=89,y=170)
signalBar = Label(device2,relief=FLAT,text = 'No information available', font='Consolas 7 bold',bg = '#006730', width=37, height=1, anchor = 'e')
signalBar.place(x=5,y=2)
displayBar = Label(device2,relief=FLAT,text = 'N/A', font='Consolas 15 bold',bg = '#006730', width=17, height=1, anchor = 'center')
displayBar.place(x=3,y=18.25)
DummyBar = Label(device2,relief=FLAT,text = '',bg = '#006730', width=2, height=1, anchor = 'e')
DummyBar.place(x=3,y=2)
t1=Thread(target=capture)
t1.start()
device2.mainloop()