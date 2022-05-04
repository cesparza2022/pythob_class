'''NAME
    porcentajes

VERSION
    1.1

AUTHOR
    César Esparza

GITHUB
  https://github.com/cesparza2022/pythob_class

DESCRIPTION
    Programa para calcular el porcentaje de AT y CG de una secuencia dada por un archivo del cual se solicita su ruta

CATEGORY
	  Genomic Sequence

ARGUMENTS
    none

'''

## Solicitar la ruta del archivo 
ruta = input("Ingrese la ruta del archivo\n")

try:

  ## Se abre el archivo para leer
  with open(ruta, 'r') as dna:
        arreglo= dna.read()
        
except IOError as io_error: 
    print(f"No se encuentra el archivo {io_error} \n")
  
else:

  ##Calcular e imprimir los porcentajes 
  print(f'Porcentaje de GC y AT\n  AT:{((arreglo.count("A") + arreglo.count("T"))/len(arreglo))*100 }% GC:{((arreglo.count("G") + arreglo.count("C"))/len(arreglo))*100 }%')