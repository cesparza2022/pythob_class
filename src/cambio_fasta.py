''' 
NAME
    cambio_fasta
    
VERSION
    1.1
    
AUTHOR 
    César Esparza

GITHUB
  https://github.com/cesparza2022/pythob_class
    
DESCRIPTION
    Programa que genera un archivo fasta apartir de un archivo que contiene una secuencia de ADN.
    
CATEGORY
	  Genomic Sequence

ARGUMENTS
    none
    
'''
ruta = input("ingrese la ruta del archivo: ")

try:
    with open( ruta,'r') as dna:
        arch= dna.read()
        
except IOError as io_error: 
    print(f"No se encuentra el archivo {io_error} \n")


else:
  ## Se solicita el identificador de la secuencia 
  id = input("ID de la secuencia ")

  ## Se genera el nuevo archivo fasta
  fasta= open("results/arreglo.fasta","w")
  fasta.write(f">{id}\n")
  fasta.write(arch)
  fasta.close()