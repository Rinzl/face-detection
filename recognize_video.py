# USAGE
# python recognize_video.py --detector face_detection_model \
#	--embedding-model openface_nn4.small2.v1.t7 \
#	--recognizer output/recognizer.pickle \
#	--le output/le.pickle

# import the necessary packages
# from imutils.video import VideoStream
# from imutils.video import FPS
# import numpy as np
import argparse
# import imutils
import pickle
import time
# import cv2
import os
import urllib.request
import time
import threading
import requests

class myThread (threading.Thread):
	def __init__(self, fileName):
		threading.Thread.__init__(self)
		self.fileName = fileName
	def run(self):
	   files = {'file': open(self.fileName, 'rb')}
	   r = requests.post(urlUpload, files=files)
	   print(r)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-H", "--host", type=str, required=True,
	help="Host to camera")
ap.add_argument("-P", "--post", type=str, required=True,
	help="Post to camera")
ap.add_argument("-U", "--upload", type=str, required=True,
	help="Post to Server")
args = vars(ap.parse_args())

# initialize the video stream, then allow the camera sensor to warm up
print("[INFO] starting video stream...")
url = "http://" + args["host"] + ":" + args["post"] +"/shot.jpg"
print("connnect to " + url)
urlUpload = 'http://'+ args["upload"]+':4555/upload'
print('server : ' + urlUpload)
# vs = VideoStream(src="rtsp://192.168.0.12:8080/h264_ulaw.sdp").start()
# vs = VideoStream(src=url).start()
time.sleep(2.0)

# start the FPS throughput estimator
# fps = FPS().start()

# loop over frames from the video file stream
while True:

	fileName = "output-demo/face"+ str(int(round(time.time() * 1000))) +".jpg"
	print("Save file " + fileName)
	looopCount = 0
	urllib.request.urlretrieve(url, fileName)
	# thread = myThread(fileName)
	# thread.start()
	time.sleep(2.0)