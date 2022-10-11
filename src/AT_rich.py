'''
NAME
    AT_rich
VERSION
    1.0
    
AUTOR
	César Esparza
 
DESCRIPTION
   Busca la región más rica en AT
    
CATEGORY
    DNA
    
ARGUMENTS
    -h, --help
    -f, --file  archivo con secuencia de ADN a leer.
    -s [int] tamaño de la región rica en AT.
    
SOFTWARE REQUIREMENTS
    Python 3.10
    
INPUT
    Archivo de DNA
    Tamaño mínimo de las regiones
    
OUTPUT
    Posición de las regigones ricas en AT.
'''
# Importamos librerias
from Bio_tools import validate_dna, max_pattern, index_list
import argparse
import re 

# Paso de argumentos mediante argparse
arg_parser = argparse.ArgumentParser(description="Busca las regiones ricas en AT")
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="Archivo de DNA",
                    required=True)
         
arg_parser.add_argument("-s", "--search",
                    help="Tamaño mínimo",
                    type=int,
                    required=False)



args = arg_parser.parse_args()

#Definimos el patron 
pat = "[AT]+"

#Extraemos la secuencia el archivo 
with open(args.file, "r") as file:
    seq = file.read()
    
#validamos la secuencia  
seq = validate_dna(seq)

#si la secuencia es valida corremos el ciclo
if seq:
  if search:
    max_pattern(seq,pat,args.search)
  else: max_pattern(seq,pat)
    
#Si la secuencia no esta limpia se imprimen los indices de los caracteres invalidos
else:
  show_novalid(seq)
  

  







