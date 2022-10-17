'''
NAME
    Genbank introduction
VERSION
   1.0
AUTHOR
    César Esparza
DESCRIPTION
    Devuelve el nombre, fecha, organismo, país, locación
USAGE
    py src/GNBNK_into.py
ARGUMENTS
'''
from Bio import SeqIO

for record in SeqIO.parse("data/virus.gb", "genbank"):
   print(f"nombre:{record.name}\n")
   print(f"fecha:{record.annotations['date']}\n")
   print(f"organismo: {' '.join(record.features[0].qualifiers['organism'])}\n")
   print(f"país: {' '.join(record.features[0].qualifiers['country'])}\n")
   print(f"locación: {record.features[0].location} Tipo: {record.features[0].type}\n")
