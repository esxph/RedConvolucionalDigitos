
from CNN.utils import *

from tqdm import tqdm
import argparse
import matplotlib.pyplot as plt
import pickle

from PIL import Image;
import io;


#Programa para probar una imagen con la red neuronal

def test(archivo):

	WIDTH = 28
	#Abre la imagen, cambia tamanio y lo convierte a un arreglo 
	img = Image.open(archivo).convert('L')
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

	print(pred)




test('numero3.png')