Link to install dlib and cmake in windows:
https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/



About code:
**os.path.splitext(cl) :its a method used to split the path name into pair of root and extension
here we only accessing the filename 

**os.listdir(path)  :gives list of all the files and directories inside the path
**cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  :converts the image color into RGB

**# Displaying the image 
        cv2.imshow("uploaded image after conversion", image)

**https://face-recognition.readthedocs.io/en/latest/face_recognition.html  for more details on face recognition

**face_recognition.face_encodings(img) :A list of 128-dimensional face encodings (one for each face in the image) since we encoding each image one by one we are accepting only [0] output encoding

**cv2.VideoCapture(0) :for video capturing


**face_recognition.face_locations(imgS):  gives list of all face location in the css

**face_recognition.compare_faces(encodeListKnown, encodeFace,tolerance=0.6)
        : To compare the list of encodings of the faces with the captured image from webcam


**face_recognition.face_distance(encodeListKnown, encodeFace)   :
             euclidean distance for each comparison face.which acutually tells about how close they are related


