import cv2, time

my_image = cv2.imread("a.jpg", 1) #reading an image, converts to numpy array

def PrintImageArray():
	print(my_image.shape) # shape displays the size of the image

def ShowImage(image):
	cv2.imshow("TheBoss", image) #pass in a numpy array and it builds in an image
	cv2.waitKey(2000) #waits for 2 seconds before closing the window
	cv2.destroyAllWindows() #accesses the waitkey function to destroy the windows

def ShowVideo(frame):
	cv2.imshow("eachFrame", frame)

def ResizeImage():
	resized = cv2.resize(my_image, (int(my_image.shape[1]/2),int(my_image.shape[0]/2)))
	ShowImage(resized)

def FaceDetect(frame):
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #C:\Users\anuku\Anaconda3\lib\site-packages\cv2\data\
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5) # searches for the face rectangle coordinates
	# scalefactor decreases shape value by 5 percent until the face is found
	for x,y,w,h in faces:
		gray_img = cv2.rectangle(gray_img, (x,y), (x+w,y+h), (0,255,0), 3)
	ShowVideo(gray_img)

def CaptureVideo():
	video = cv2.VideoCapture(0)
	while True:
		check, frame = video.read() #check is the bool if video.read has captured the video object 
		# or not and frame is the first frame of the video
		FaceDetect(frame)
		#time.sleep(3) # video is captured for 3 seconds
		key = cv2.waitKey(10)
		if key == ord('a'):
			break
	video.release()
	cv2.destroyAllWindows()
CaptureVideo()