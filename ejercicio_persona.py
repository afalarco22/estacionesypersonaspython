edadPersona = int(input("Ingrese la edad de la persona "))

op = 1

while op != 0:
    if(edadPersona > 0 and edadPersona <= 5):
        print("La persona se clasifica en primera infancia")
    elif(edadPersona > 5 and edadPersona < 12):
        print("La persona está clasifica en primera infancia")
    elif(edadPersona >=12 and edadPersona < 18):
        print("La persona está clasifica en adolesencia")
    elif(edadPersona >= 18 and edadPersona < 28):
        print("La persona está clasifica en juventud")
    elif(edadPersona >= 18 and edadPersona < 60 ):
        print("La persona está clasifica en adulto")
    elif(edadPersona >= 60 and edadPersona < 120):
        print("La persona está clasifica en persona mayor")
    else:
        print("El rango de edad es erroneo")
    op = int(input("Ingrese cero para salir del programa, otro numero para continuar"))

print("Fin del programa")

