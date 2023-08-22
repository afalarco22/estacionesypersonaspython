op = 1
while op != 0:

    dia = int(input("Ingrese el día: "))
    mes = int(input("ingrese el mes del año: "))

    if((mes == 1 and(dia > 0 and dia <= 31)) 
       or (mes == 2 and(dia > 0 and dia <=28)) 
       or (mes == 3 and(dia > 0 and dia <= 20))):
        
        print("La temporada de la fecha ingresada es invierno")

    elif((mes == 3 and(dia > 20 and dia <= 30)) 
      or (mes == 4 and(dia > 0 and dia < 31)) or (mes == 5 and(dia > 0 and dia <= 31)) 
      or ( mes == 6 and(dia > 0 and dia <= 10))):
        
        print("La temporada de la fecha ingresada es verano")

    elif((mes == 6 and(dia >10 and dia <= 30)) 
     or (mes == 7 and(dia > 0 and dia <= 31)) or 
     (mes == 8 and(dia > 0 and dia <= 31)) 
     or(mes == 9 and(dia > 0 and dia <= 25))):
        
        print("La temporada de la fecha ingresada es otoño")

    elif((mes == 9 and(dia > 25 and dia <= 30)) or (mes == 10 and(dia > 0 and dia <= 31)) 
         or (mes == 11 and(dia > 0 and dia < 31))):
        print("La fecha ingresada es primavera")
    else:
        print("La fecha ingresada no es correcta")
    op = int(input("Ingrese la el cero (0) para salir, otro valor para continuar"))

print("fin del programa")




