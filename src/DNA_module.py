'''
NAME
    DNA_module
VERSION
    2.1
AUTHOR
    César Esparza
GITHUB
    https://github.com/cesparza2022/pythob_class.git
DESCRIPTION
    Herramientas para el manejo de secuencias de DNA
CATEGORY
    DNA sequence
 
 Functions
    validate
    frequency
    transcription
    reverse_complement
    purine_pyrimidine
    read
    translate
    

'''
from structures import nulceotides, reverse_nucleotides
 
    
def validate(dna_seq):
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
    codon = codons[seq[pos:pos+3]]
    prot.append(codon)

  return prot

def longest_peptide(seq):
    
      '''
    Regresa el peptido mas largo encontrado en la 
        secuncia dada:
            seq (str): secuencia de DNA a procesar
        Returns:
            long_peptide (str): la secuencia que resulta en 
                el peptido mas largo
    '''
    rev_seq = reverse_complement(seq)
    
    orfs = SeqUtils.nt_search(str(seq), 'ATG')   
    rev_orfs = SeqUtils.nt_search(str(rev_seq), 'ATG')
    
    peptids = [seq[nuc:].translate(to_stop = True) for nuc in orfs[1:]]
    peptids.append([rev_seq[nuc:].translate(to_stop = True) for nuc in rev_orfs[1:]])
    
    return max(peptids)
    
    
    
  

  
