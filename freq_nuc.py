'''
NAME
    freq_nuc
VERSION
    1.0
AUTHOR
  César Esparza
GITHUB
  https://github.com/cesparza2022/pythob_class
DESCRIPTION
  El codigo imprime la frecuencia de cada       nucleotido en una secuencia ingresada por     el usuario

'''
##Preguntar al usuario si quiere ingresar el arreglo de forma manual o con el del archivo  
print ("¿Quiere ingresar el arreglo o con el del archivo dna.txt?:")
print("manual  ,  archivo")
respuesta = input(": ")

##Usar if para empezar distintos procedimietnos dependiendo de como quiera pasar el arreglo  
if respuesta == "manual":
  arreglo = input("ingrese el arreglo: ")
else:
#Obtener el archivo desde la ruta 
  arch = open("data/dna.txt", "r")
  arreglo = arch.read()
  arch.close()


##Imprimir la fecuencia de cada nucleotido
print(f'Freceuncia de nucleotidos\n" {str(arreglo)}\n A: {arreglo.count("A")} C: {arreglo.count("C")} T: {arreglo.count("T")} G: {arreglo.count("G")}')


