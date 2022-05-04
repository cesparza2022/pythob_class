'''
NAME
    freq_nuc

VERSION
    1.1

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
##Solicitar al usuario que ingrese el arreglo 
arreglo = input("ingrese el arreglo: ")


##Imprimir la fecuencia de cada nucleotido
print(f'Freceuncia de nucleotidos\n" {str(arreglo)}\n A: {arreglo.count("A")} C: {arreglo.count("C")} T: {arreglo.count("T")} G: {arreglo.count("G")}')


