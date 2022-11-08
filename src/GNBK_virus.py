'''
NAME
	GNBNK_virus
    
VERSION
    2.0
    
AUTHOR
	César Esparza
    
DESCRIPTION
   Obtener los datos generales y genes particulares del archivo dado
    
CATEGORY
	Gene bank
    
ARGUMENTS
    -h --help
    -f --FILE
    -g --GENES

SEE ALSO 
    none
  
'''
from Bio import SeqIO
from Bio_tools import transcription,translate
import argparse

arg_parser = argparse.ArgumentParser(description="Desglossar la información de un archivo gene bank")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo genebank del organismo",
                    required=True)
                    
arg_parser.add_argument("-g","--GENES",
                    help = "Los genes que se deben buscar",
                    type = list,
                    nargs = '+',
                    required= True)
                    
args= arg_parser.parse_args()

for record in SeqIO.parse(args.FILE, "genbank"):
  print(f"nombre:{record.name}\n")
  print(f"fecha:{record.annotations['date']}\n")
  print(f"organismo: {' '.join(record.features[0].qualifiers['organism'])}\n")
  print(f"país: {' '.join(record.features[0].qualifiers['country'])}\n")
  print(f"locación: {record.features[0].location} Tipo: {record.features[0].type}\n")
  for gene in args.GENES: 
     for feature in gb_record.features: 
        if feature.type == args.GENES:
          if features.qualifiers["gene"][0] == gene:
            print(f"{args.gene} information: \n")
            seq = gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end]
            print(f'Secuencia: {seq}\n')
            print(f'Transcripción: {transcription(seq)})
            print(f'Traducción: {translate(seq)}')
