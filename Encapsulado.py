import RPi.GPIO as GPIO #volvemos a importar la libreria para ejecutar el estado de los pines
import time
def pulsador(bandera):	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(12, GPIO.OUT)
	if GPIO.input(11) == GPIO.LOW:	#leemos el pin del pulsador para poder entrar a cambiar a la bandera, para luego enviarla a LedPULL para realizar la tarea que cambia el estado del led
		bandera = not bandera
		time.sleep(0.3)
	if bandera == True: #dependiendo del estado de la bandera que recibimos realizamos el cambio del estado del led a HIGH o LOW
		GPIO.output(12, GPIO.HIGH)
		print('Led encendido')
	if bandera == False:
		GPIO.output(12, GPIO.LOW)
		print('Led apagado')
	return (bandera) #Terminamos la tarea y enviamos a que se acepto la bandera, como tambien que la tarea fue realizada

