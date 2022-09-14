'''
NAME: 
    RNA_to_Protein
    
VERSION:
    1.0
    
AUTOR: 
    César Esparza
    
DESCRIPTION: 
    Script que traduce una secuencia de DNA o RNA en 
    una secuencia protéica
    
USAGE: 
    python RNA_to_prot.py [-h] -s secuencia RNA
    
ARGUMENTS: 
    -h, --help           
    -s, --string         
    -f --file, --file path/to/file 
    -o --out_file
                        
SOFTWARE REQUIREMENTS: 
    python 3.10
    
INPUT: 
    secuencia de RNA o DNA
    archivo con RNA o DNA
    
OUTPUT: 
    cadena de aminoácidos
'''
# Importar libreirias
import argparse
from Bio_tools import validate_rna
from Bio_tools import translate_rna
from Bio_tools import read
from Bio_structures import nucleotides
from Bio_structures import gencode 

# Pase de argumentos
arg_parser = argparse.ArgumentParser(description="Translating ARN to protein")

# Obtiene la secuencia de un archivo  
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="Archivo con la secuencia de ARN o ADN",
                    required=False)
              
# Recibe la secuencia ingresada con el teclado 
arg_parser.add_argument("-s", "--string",
                    help="Secuencia de ARN o ADN",
                    type=str,
                    required=False)   

# Direccion de archivo con el output
arg_parser.add_argument("-o", "--out_file",
                    help="Archivo de salida",
                    required=False)


arguments = arg_parser.parse_args()


# Utiliza la secuencia almacenada en el archivo
# Lee, valida y traduce
if arguments.file:
  raw_sequence = read(arguments.file)
  val_sequence = validate(raw_sequence)
  peptide = translate(val_sequence)

# Utiliza la secuencia ingresad con el teclado
# Valida y traduce  
if arguments.string:
  raw_sequence = arguments.string
  val_sequence = validate(raw_sequence)
  peptide = translate(val_sequence)
  
# Escribe el reultado en un archivo 
if arguments.out_file:
  out_file = open(arguments.out_file, 'w')
  out_file.write(f"La secuencia resultante es:\n{''.join(peptide)}")
  out_file.close()

# Imprimir la secuencia
if peptide:
  print(f"La secuencia resultante es:\n {peptide}")
  
  
  
  





