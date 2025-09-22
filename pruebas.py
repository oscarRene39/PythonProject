def get_buscar(): #mi primera funcion print
    print("Hello World")# imprime
    ciclo=input("Ingrese el dato a buscar: ") #pide un dato y lo almacena
    fecha=input("Ingrese la fecha: ")
    return ciclo,fecha

def main():
    buscar = get_buscar()
    print(buscar)

main()
