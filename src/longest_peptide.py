'''
Name 
    longest_peptide
    
Version
    1.1
    
Author 
    César Esparza
    
Descripcion
    Script que busca la cadena peptidadica de mayor longitud en un archivo con una secuencia genomica.
    
Category
    Genomic
    Prtoteic
    
Arguments

    
See also
    None
'''

from DNA_module import tranaslate, validate, seq_read
from Bio import SeqUtils
import argparse


arg_parser = argparse.ArgumentParser(description="Buscar el peptido mas largo")
                    
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="dirección al archivo",
                    required=False)

arg_parser.add_argument("-s", "--sequence",
                    help="secuencia de DNA",
                    required=False)
                    
arguments = arg_parser.parse_args() 

if arguments.sequence:
   secuencia = arguments.sequence
    
if arguments.file:
   secuencia = seq_read(arguments.sequence)

if validate(secuencia):
    long_peptide=longest_peptide(seceuncia) 
    print(f"el peptido de mayor longitud encontrado en la secuencia es {long_peptide}")







