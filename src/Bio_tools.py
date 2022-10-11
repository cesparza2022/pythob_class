'''
NAME
    Bio_tools
VERSION
    1.5
AUTHOR
    César Esparza
GITHUB
    https://github.com/cesparza2022/pythob_class.git
DESCRIPTION
    Herramientas para el manejo de secuencias de DNA y RNA
CATEGORY
    DNA & RNA sequence
 
 Functions
    validate_dna
    validate_rna
    frequency
    transcription
    max_pattern
    index_list
    show_novalid
    reverse_complement
    purine_pyrimidine
    read
    translate
    
'''
from structures import nulceotides, reverse_nucleotides
import re 
    
def validate_dna(dna_seq):
    '''
    Pasa a mayúsculas y revisar que sean valores validos 
        Parameters:
            dna_seq (str): secuencia de DNA a procesar
        Returns:
            tmpseq (str): secueancia de DNA validada o error 
    '''
  tmpseq = dna_seq.upper()
  for nuc in tmpseq:
    if nuc not in nucleotides:
      print("Esta mal el arreglo")
      return 
  return tmpseq

   
def validate_rna(rna_seq):
    '''
    Pasa a mayúsculas y revisar que sean valores validos 
        Parameters:
            dna_seq (str): secuencia de RNA o DNA a procesar
        Returns:
            tmpseq (str): secueancia de RNA validada o error 
    '''
  tmpseq = rna_seq.upper()
  for nuc in tmpseq:
    if nuc not in nucleotides:
      print("Esta mal el arreglo")
  tmpseq = tmpseq.replace("T","U")
  return(tmpseq)
  

def frequency(seq): 
      '''
    Regresa el conteo de nucleotidos en una secuencia de DNA
        Parameters:
            seq (str): secuencia de DNA a procesar
        Returns:
            tmpFreqDict (dicc): secueancia de DNA validada o error 
    '''  
  tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
  for nuc in seq: 
     if (nuc in tmpFreqDict): 
      tmpFreqDict[nuc] += 1
     else:
        tmpFreqDict[nuc] = 1 
  return tmpFreqDict

 
def transcription(seq):
          '''
    Cambia la cadena de DNA una de RNA 
        Parameters:
            seq (str): secuencia de DNA a procesar
        Returns:
            (str): secuancia de RNA
    '''  
  return seq.replace("T","U")


def reverse_complement(seq):
          '''
    Regresa la cadena complementaria
        Parameters:
            seq (str): secuencia de DNA a procesar
        Returns:
            (seq): secuencia de DNA complentaria a la ingresada
    '''  
  return"".join( reverse_nucleotides[nuc] for nuc in seq)

def max_pattern(seq, pattern, min_size=2)
 '''
    Regresa el numero de maximo de repeticiones consecutivasa
        de un patron a lo largo de la cadena 
        Parameters:
            seq (str): secuencia de DNA en la que buscar
            pattern (str): patron a buscar
            size_min (int): numero minimo de repeticiones del patron 
        Returns:
            (int): mayor numero e repeticiones consecutivas encontradas
       '''  
  temp_list=[]
  result = re.finditer(pattern,seq)
  for pat in result:
    size = pat.end() - pat.start()
    temp_list.append(size)
  if max(temp_list) >= min_size:
    return (max(temp_list))
  else:
    print(f"no se encontro el patron un minimo de {min_size} veces ")
    return 
    
def show_novalid(seq):
    '''
    Regresa los indices de los caracteres invalidos de la secuencia 
        Parameters:
            seq (str): secuencia de DNA en la que buscar 
        Returns:
              (str): el caracter invalido y sus indices
       ''' 
    not_nucs = []
    for nuc in seq:
      if nuc not in nucleotides:
        not_nucs.append(nuc) 
    for not_nuc in not_nucs:
      while not_nucs.count(not_nuc) > 1:
        not_nucs.remove(not_nuc)  
    for not_nuc in not_nucs:
       print(f"el caracter {not_nuc} se encontro en las posiciones {index_list(not_nuc,seq)}")
    return 1
    

def index_list(pattern, seq):
   '''
    Regresa los indices de un patron en una secuencia dada
        Parameters:
            seq (str): secuencia de DNA en la que buscar 
            pattern (str): patron que buscar en la secuencia
        Returns:
              (list): inices en los que se encontro el patron 
       ''' 
  return [n for n,item in enumerate(seq) if item==pattern]

def purine_pyrimidine(seq, dec=0):
          '''
    Regresa los procentajes de AT y GC 
        Parameters:
            seq (str): secuencia de DNA a procesar
            dec (int): cuantos decimales se desean, por default cero
        Returns:
            at_content (float): porcentaje de purinas en la secuencia
            gc_content (float): porcentaje de pirimidinas en la secuencia
    '''  
  a_num = seq.count('A') 
  t_num= seq.count('T')
  c_num= seq.count('C') 
  g_num = seq.count('G')

  long = len(seq) 
  
  if dec:
      at_content = round(( (a_num + t_num) / long)*100, dec) 
      cg_content = round(((c_num + g_num) / long)*100, dec) 
  else:
      at_content = (( a_num + t_num) / long) *100
      cg_content = ((c_num + g_num) / long) *100
     

  return at_content,cg_content

  
def read(file_path):
          '''
    Se encarga de la lectura del archivo 
        Parameters:
            file_path (str): ruta al archivo 
        Returns:
             (list): lectura por linea del archivo 
    '''  
  with open(file_path, 'r') as archivo:
    return [l.strip() for l in archivo.readlines()]
   
    
def translate(seq, pos_i =0):
          '''
    Regresa la traduccion de la secuencia de DNA
        Parameters:
            seq (str): secuencia de DNA a procesar
            pos_i (int): nuc de inicio para cambia marco de lectura
        Returns:
            prot (list): secuencia peptídica
    '''  
  prot = []
  for pos in range(pos_i, len(seq) -2, 3): 
    codon = gencode[seq[pos:pos+3]]
    prot.append(codon)

  return prot
