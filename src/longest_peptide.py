'''
Name 
    longest_peptide
    
Version
    0.1
    
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

from DNA_module import tranaslate
from Bio import SeqUtils
import argparse


arg_parser = argparse.ArgumentParser(description="Buscar el peptido mas largo")
                    
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ADN",
                    required=False)

arg_parser.add_argument("-s", "--SEQUENCE",
                    help="secuencia de ADN a procesar",
                    type = Seq,
                    required=False)
                    
arguments = arg_parser.parse_args() 

##Validar la secuencia 

##Llamar a la funcion longest_peptide

##Imprimir el resultado 








