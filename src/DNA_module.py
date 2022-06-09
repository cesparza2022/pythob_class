'''
NAME
    DNA_module
VERSION
    1.8
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

nucleotides = ["A", "T","C","G"]
reverse_nucleotides = {"A":"T", "T":"A","C": "G","G":"C"}

#Pasa a mayúsculas y revisar que sean valores validos       
def validate(dna_seq):
  tmpseq = dna_seq.upper()
  for nuc in tmpseq:
    if nuc not in nucleotides:
      print("Esta mal el arreglo")
      return 
  return tmpseq
  
#Cuenta cuantas veces se repite cada nucleotido
def frequency(seq): 
  tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
  for nuc in seq: 
     if (nuc in tmpFreqDict): 
      tmpFreqDict[nuc] += 1
     else:
        tmpFreqDict[nuc] = 1 
  return tmpFreqDict

  #Cambia ADN a ARN
def transcription(seq):
  return seq.replace("T","U")

  # Saca la cadena complementaria  
def reverse_complement(seq):
  return"".join( reverse_nucleotides[nuc] for nuc in seq)

  #Regresa el porcentaje de 
def purine_pyrimidine(seq, dec=0):
  
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

  #Regresa la lectura dell archivo 
def read(file_path):
  with open(file_path, 'r') as archivo:
    return [l.strip() for l in archivo.readlines()]
   
    #Regresa la traduccion de la secuencia
def translate(seq, pos_i =0):
  prot = []
  for pos in range(pos_i, len(seq) -2, 3): 
    codon = codons[seq[pos:pos+3]]
    prot.append(codon)

  return prot
  

  
