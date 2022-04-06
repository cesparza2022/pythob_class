'''
NAME
    porcentajes
VERSION
    1.0
AUTHOR
  César Esparza
GITHUB
  https://github.com/cesparza2022/pythob_class
DESCRIPTION
  El codigo sirve calcular los porcentajes de   GC y AT en el arreglo ingresado por el        usuario

'''
#Obtener el archivo desde la ruta 
arch = open("data/dna.txt", "r")
arreglo = arch.read()
arch.close()


##Calcular e imprimir los porcentajes 
print(f'Porcentaje de GC y AT\n  AT:{((arreglo.count("A") + arreglo.count("T"))/len(arreglo))*100 }% GC:{((arreglo.count("G") + arreglo.count("C"))/len(arreglo))*100 }%')