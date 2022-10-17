'''
NAME
  Umbral
VERSION
  1.0
AUTOR
	César Epsarza
DESCRIPTION
  Devuelve un archivo con las secuencias cuyas bases
  superen cierto control de calidad.

ARGUMENTS
  -u --UMBRAL: número que determine el umbral de calidad.
  -f --FILE: path/to/file fastq
  -o --OUTPUT: path/to/file fastq
    
OUTPUT
    ./data/arriba_umbral

USAGE
    py src/umbral.py

'''

# Importar librería
from Bio import SeqIO
import argparse
from Bio_tools import fastq_score

#Hacer pase de argumentos 
arg_parser = argparse.ArgumentParser(description="Busacar que superen el score mínimo")
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file fastq",
                    help="Dirección al archivo",
                    required=True)

arg_parser.add_argument("-u", "--UMBRAL",
                    type= int,
                    help="El score mínimo que debe superar",
                    required=True)

arg_parser.add_argument("-o", "--OUTPUT",
                    metavar="path/to/file fastq ",
                    help="Dirección archivo de salida",
                    required=False)

args = arg_parser.parse_args()

if args.FILE && args.UMBRAL:
  if args.OUTPUT:
    fastq_score(args.FILE, args.UMBRAL, args.OUTPUT)
  else:
    fastq_score(args.FILE, args.UMBRAL)

    
else:
  print("faltan datos")
    


