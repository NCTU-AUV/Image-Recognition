import cv2
import numpy as np
import os
from keras.preprocessing.image import ImageDataGenerator

def Augmentation(directory, filename):
	
	img = cv2.imread(filename)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = img.reshape((1,) + img.shape)

	try:
		if not os.path.exists(directory+"aug"):
			os.makedirs(directory+"aug")
		
		datagen = ImageDataGenerator(zca_whitening=False, rotation_range=10, width_shift_range=0.1, height_shift_range=0.1, channel_shift_range = 100, \
									brightness_range = [0.6, 0.8], shear_range=0.1, zoom_range=0.1, horizontal_flip=False, fill_mode='nearest')

		cnt = 0
		for batch in datagen.flow(img, batch_size=10, save_to_dir=directory+"aug/", save_format='png'):
			aug_img = batch[0]
						
			aug_img = aug_img.astype('float32')
			aug_img /= 255
			cnt += 1
			if cnt > 10:
				break
	except:
		print("Adjusting image "+filename+" error!")

def run(directory):
	for f in os.listdir(directory):
		if f.lower().endswith((".jpg", ".png")):
			print("Adjusting image "+f)
			Augmentation(directory, directory+f)

run("E:/darknet/test/data/img/resize/")