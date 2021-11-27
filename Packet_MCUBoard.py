from gpio import *
#Asignar puertos digitales en placa mcu
luz = 0
#puerta=1
sirena=2
#ventana=3
regadera=4
#garage=5
while True:
	puerta = customRead(1)
	ventana = customRead(3)
	garage = customRead(5)
	if garage == "1" or puerta == "1,0" or ventana == "1":
		customWrite(luz,"2")
		customWrite(sirena,"1")
		customWrite(regadera,"1")
		

	else:
		customWrite(luz,"0")
		customWrite(sirena,"0")
		customWrite(regadera,"0")
