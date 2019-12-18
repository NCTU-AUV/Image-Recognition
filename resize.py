import cv2
import os

cnt = 0

def resize(directory, filename):
	global cnt
	img = cv2.imread(filename)
	rz_img = cv2.resize(img, (400, 300))

	try:
		if not os.path.exists(directory+"resize"):
			os.makedirs(directory+"resize")

		cv2.imwrite(directory+"resize/"+str(cnt)+"_door.png", rz_img)
		cnt += 1
	except:
		print("Resizing image "+filename+" error!")

def run(directory):
	for f in os.listdir(directory):
		if f.lower().endswith((".jpg", ".png")):
			print("Resizing image "+f)
			resize(directory, directory+f)

run("E:/darknet/test/data/img/")