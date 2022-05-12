'''NAME
    porcentajes

VERSION
    1.3

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
import argparse

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
args = parser.parse_args()

ruta = args.input

try:

  ## Se abre el archivo para leer
  with open(ruta, 'r') as dna:
        arreglo= ruta.read().rstrip("\n").upper()
	size = len(arreglo)
        
except IOError as io_error: 
    print(f"No se encuentra el archivo {io_error} \n")
  
else:
    ## Se saca el porcentaje de la secuencia y se guarda en variables
    AT = ((arreglo.count('A') + arreglo.count('T')) / size) * 100
    GC = ((arreglo.count('G') + arreglo.count('C')) / size) * 100
	 
    if args.round:
        AT = round(AT, args.round)
        GC = round(GC, args.round)
    
    if args.output:	
	file = open(args.output, "w")
	try:
   		file.write(f"La secuencia {arreglo}\n Tiene un porcentaje de {AT}% de AT y {GC}% de GC" )
		print(f"\nSe genero el archivo {args.output} con los resultados")
	finally:
		file.close()  
    
    else:		
	print(f"Los porcentajes son:\n  AT:{AT}% y GC:{GC}%" 
                    

    
	
    
