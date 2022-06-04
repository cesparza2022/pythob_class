'''
NAME
    freq_nuc

VERSION
    2.0

AUTHOR
  César Esparza

GITHUB
  https://github.com/cesparza2022/pythob_class
DESCRIPTION
    El codigo imprime la frecuencia de cada nucleotido en una secuencia ingresada por el usuario

CATEGORY
	  Genomic Sequence

ARGUMENTS
    none

'''
## Importar funcion 
from DNA_module import frequency

##Solicitar al usuario que ingrese el arreglo 
arreglo = input("ingrese el arreglo: ")


##Imprimir la fecuencia de cada nucleotido
print(frequency(arreglo))


