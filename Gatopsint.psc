Algoritmo Gato
	turno<-1
	tiros<-1
	Dimension tablero[3,3]
	Para i<-1 Hasta 3 Con Paso 1
		Para j<-1 Hasta 3 Con Paso 1
			tablero[i,j]<-' '
		FinPara
	FinPara
	
	Mientras tiros<=9 Hacer
		Escribir "Turno del jugador ", turno, " Indique el renglon (1-3)"
		leer r
		Escribir "Indique la columna (1-3)"
		leer c
		Si(tablero[r,c] =' ') Entonces
			Si( turno=1) Entonces
				tablero[r,c] <- 'X'
			    turno <- 2
			SiNo
			    tablero[r,c] <- 'O'
			    turno <- 1
			FinSi
			tiros <- tiros+1
		SiNo
			Escribir "Repetir el turno y seleccione una opcion que este libre..."
		FinSi
		
		Escribir "같같같같같같같같같�"
		Para i<-1 Hasta 3 Con Paso 1
			Para j<-1 Hasta 3 Con Paso 1
				Escribir tablero[i,j],"," Sin Saltar
			FinPara
			Escribir ""
		FinPara
	FinMientras
	
FinAlgoritmo
