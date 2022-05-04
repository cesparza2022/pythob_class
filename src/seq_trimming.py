"""
NAME
        seq_trimming
        
VERSION
        1.1
        
AUTHOR
        César Esparza

GITHUB
  https://github.com/cesparza2022/pythob_class
        
DESCRIPTION
        Elimina los adaptadores de las secuencias
                
CATEGORY
	    Genomic Sequence

ARGUMENTS
        none
    
"""

## Solicitar la ruta del archivo      
ruta = input("ingrese la ruta del archivo: ")

try:
    with open( ruta,'r') as dna:
        lineas = dna.readlines()

except IOError as io_error:
    print(f"No se encuentra el archivo {io_error} \n")

else:
     with open("resultados/.txt", 'w') as adapter_free:
        ## Eliminar los adaptadores.
        ## Pasar la secuencia limpia a otro archivo
        for seq in lineas:
            seq_limpia = seq[14:]
            adapter_free.write(seq_limpia)


        ## Imprimir la ubicación del archivo con el resultado
        print("El archivo con el output esta en el directorio de resultados con el nombre 'adapter_free.txt'")
