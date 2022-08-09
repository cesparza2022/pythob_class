'''NAME
    porcentajes

VERSION
    2

AUTHOR
    César Fernando Esparza Alvarado

GITHUB
  https://github.com/cesparza2022/pythob_class

DESCRIPTION
    Programa para calcular el porcentaje de AT y CG de una secuencia dada por un archivo del cual se solicita su ruta

CATEGORY
	  Genomic Sequence

ARGUMENTS
    none

'''
# Importar
import argparse
from DNA_module import validate, purine_pyrimidine

## Definir los argumentos opcionales y posicionales 
arg_parse = argparse.ArgumentParser( description="Calcula los porcentajes de AT y GC")

arg_parse.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

arg_parse.add_argument("-o", "--output",
                    help="Path for the output file",
                    required=False)

arg_parse.add_argument("-r", "--round",
                    help="number of digits to rouond",
                    type=int,
                    required=False)

## Leer los argumentos y asignar la ruta 
args = parser.parse_args()
ruta = args.input

try:

  ## Se abre el archivo para leer, se eliminan los saltos de linea y se pone todo en mayusculas
  with open(ruta, 'r') as dna:
        arreglo= ruta.read().rstrip("\n")
	arreglo = validate(arreglo)
	
## Marca Error si no se encuentra el archivo       
except IOError as io_error: 
    print(f"No se encuentra el archivo {io_error} \n")
  
else:
    ## Se saca el porcentaje de la secuencia y se guarda en variables
    cont = purine_pyrimidine(arreglo)

    ## Se redondea si el numero de decimales es asignado
    if args.round:
      cont =  purine_pyrimidine(arreglo,args.round)
   
    ## Se abre el archivo con los resultados 
    if args.output:	
	file = open(args.output, "w")
   		file.write(f"La secuencia {arreglo}\n Tiene un porcentajes de {cont} )
		print(f"\nSe genero el archivo {args.output} con los resultados")
		file.close()  
    
    else:
		
     ## Imprimir los porcentajes obtenidos 
	print(f"Los porcentajes son:\n {cont}" 
                    

    
	
    
