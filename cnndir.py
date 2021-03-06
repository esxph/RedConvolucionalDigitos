
from CNN.utils import *

from tqdm import tqdm
import argparse
import matplotlib.pyplot as plt
import pickle

from PIL import Image;
import io;
import os;



def getNumbers(dir):
	numList=[]
	index=0
	for filename in os.listdir(dir):
		identifiedNumber=str(test(dir,filename,index))
		if(len(identifiedNumber)>0):
			#numList.append(filename + ': ' + identifiedNumber)	
			numList.append(identifiedNumber)	
			index=index+1
	return numList	




def test(carpeta,archivo,index):

	WIDTH = 28
	#Abre la imagen, cambia tamanio y lo convierte a un arreglo
	try:
		img = Image.open(carpeta+'/'+archivo).convert('L')
		imgTemp=Image.open(carpeta+'/'+archivo)
		imgTemp.save("web/temp/2/"+str(index)+".png")
	except IOError:
		return '' 
	img_rs = img.resize((WIDTH,WIDTH))
	img_array = np.asarray(img_rs)
	Y = img_array.reshape(WIDTH,WIDTH)
	X = np.zeros((1,WIDTH,WIDTH),dtype=np.float32)
	for i in range(WIDTH):
		for j in range(WIDTH):
			X[0][i][j] = (255 - Y[i][j])/255

	params, cost = pickle.load(open('params.pkl', 'rb'))
	[f1, f2, w3, w4, b1, b2, b3, b4] = params
	pred, prob = predict(X, f1, f2, w3, w4, b1, b2, b3, b4)

	return str(pred)



