'''
NAME
	amino_content.py
    
VERSION
    1.0
    
AUTHOR
	César Esparza
    
DESCRIPTION
    Obtien el porcentaje de los aminoacidos que busques en una lista 
        
CATEGORY
	Aminoacid Sequence
    
USAGE
    py count_aminoacids.py -sec [secuencia de aminoacidos]
        
'''
from structures import aas
import argparse

parser = argparse.ArgumentParser(
    description="Da el porcentaje de un aminoacido especifico de una secuencia dada")

parser.add_argument("-s", "--secuencia",
                    help="La secuencia",
                    required=True)
parser.add_argument("-l", "--lista",
                    help="Aminoacidos que busques",
                    required=False)
parser.add_argument("-r", "--round",
                    help="Numero de decimales",
                    type=int,
                    required=False,)

args = parser.parse_args()

# Se asignan los argumentos a variables
seq = args.secuencia
amin = args.lista

def validate_aa(aa_seq):
  tmpseq = aa_seq.upper()
  for aa in tmpseq:
    if aa not in aas:
      return 0
  return tmpseq

def percentege(aa_seq, aa_list = ['A','I','L','M','F','W','Y','V'], deci = 0):
    
    percent_list = []
    long = len(aa_seq)
    aa_seq = validate(aa_seq)
    aa_list = validate(aa_list)
   
  if aa_seq & aa_list:
      for aa in aa_list:
        amino = aa_seq.count(aa)
        aa_percent = (amino / long) * 100                         
        aa_percent = round(aa_percent, deci)
        percent_list.append(aa_percent)
        
      return(percent_list)

    
