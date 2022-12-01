from tkinter import *
from PIL import Image,ImageTk
from _thread import *
import socket
from threading import *
from CART_concise import *
import DriverRecognition
import time

smartObj=CART()
def FaceRecognition():
    print("Initiating Face Recognition")
    print(DriverRecognition.webCheck())


def synch():
    flag=1
    (clientConnected, clientAddress) = serverSocket.accept()
    dataFromClient = clientConnected.recv(2048)
    dist = dataFromClient.decode()
    dist = dist.split(':')
    clientConnected.close()
    bound1 = dist[1][1:dist[1].index(',')]
    bound2 = dist[1][dist[1].index(',')+1:len(dist[1])-1]
    dist = dist[0][1:dist[0].index(',')]
    distance=int(dist)//35
    if(flag or (not t3.is_alive())):
        target=smartObj.CART(distance)
        if distance<=20:
            flag=0
            t3 = Thread(target=FaceRecognition)
            t3.start()
    
    if(int(dist)-car.winfo_x() in range(int(bound1),int(bound2))):
        background.delete("li")
        background.create_image(500, 170, image = front_light, anchor = NW, tags = 'li')
        background.create_image(30, 170, image = back_light, anchor = NW, tags = 'li')
    else:
        background.delete("li")
    t2 = Thread(target=synch)
    time.sleep(5)
    t2.start()

car = Tk()
car.title("Smart Vehicle (Car)")
width = 950
height = 500
car.geometry(str(width)+"x"+str(height)+"+-10+0")
car.resizable(False, False)
background = Canvas(width = width, height = height, highlightthickness=0, bg = 'black')
background.pack(expand = YES, fill = BOTH)
background_image = "background.png"
image = Image.open(background_image)
image = image.resize((width,height), Image.ANTIALIAS)
cover = ImageTk.PhotoImage(image)
background.create_image(0, 0, image = cover, anchor = NW)
car_img = ImageTk.PhotoImage(Image.open("car.png"))
front_light = PhotoImage(file = "front-light.png")
back_light = PhotoImage(file = "back-light.png")
background.create_image(180, 240, image = car_img, anchor = NW)
port = 8080
port_file = open("conn_to.txt", "w")
port_file.write('8080')
port_file.close()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1',port))
serverSocket.listen(5)
t1=Thread(target=synch)
t1.start()
car.mainloop()