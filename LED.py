import RPi.GPIO as GPIO		#Importamos las librerias para los pines GPIO, tiempo y uno propio (LedPULL), para simplificar le nombre se lo llama pul
import time
import Encapsulado as pul
GPIO.cleanup()
bandera = False		#limpiamos todos los pines para volverlos a inicializar 
while True:
	bandera = pul.pulsador(bandera)	#enviamos la bandera y recibimos si la tarea se ejecuto con exito
