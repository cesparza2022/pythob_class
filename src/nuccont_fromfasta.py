''' Name 
    Nucleotide content from a fasta file 
    
Version
    1.0
    
Author 
    Cesar Esparza
    
Descripcion
    Extrae el porcentaje de cada nucleotido de cada secuencia en formato fasta
    
Category
    DNA sequence
    
Usage
    Python src/nuccont_fromfasta.py -i path/to/file [-r ROUND]
    
Arguments
    -h --help
    -i --input 
    -r --round

See also
    None
    '''
 
from Tool_kit import purine_pyrimidine, return_seq

import argparse

arg_parser = argparse.ArgumentParser(description=" Extrae el porcentaje de cada nucleotido de cada secuencia en formato fasta")


arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="Archivo FASTA con las secuencias",
                    required=True)


arg_parser.add_argument("-r", "--round",
                    help="Numero de decimales",
                    type=int,
                    required=False)

args = arg_parser.parse_args()


##Solicitar la ruta al usuario
file_path = args.input

##Crear un diccionario para organizar la informacion relacionando el encabezado conll la secuencia
fasta_orden = {}

##Guardar la informacion como una lista
fasta = return_seq(file_path)

##El string que va a contener el encabezado
fasta_encabezado = ""

##Convertir la informacion para ser manejada como un diccionario
for line in fasta:
  if ">" in line:
    fasta_encabezado = line
    fasta_orden[fasta_encabezado] = ""
  else:
    fasta_orden[fasta_encabezado] += line
   
##Imprimir el encabezado con el contenido de gc_at por cada encabezado  
for (key,value) in fasta_orden.items() :
  if args.round:
    resultado = {key : purine_pyrimidine(value,args.roud)}
  
  else:
    resultado = {key : purine_pyrimidine(value)}
  
  print(resultado)
