'''
NAME
    file_module
VERSION
    1.0
AUTHOR
    César Esparza
GITHUB
    https://github.com/cesparza2022/pythob_class.git
DESCRIPTION
     Herramientas para el manejo de archivos de datos biológicos
CATEGORY
    DNA files
 
 Functions
    seq_trimming 
    fasta_generator
'''

 #Remueve los adaptadores 
def seq_trimming(file_path, new_path="data/trimmed_seq.txt"):
  with open( file_path,'r') as dna:
        lineas = dna.readlines()
  with open(new_path, 'w') as adapter_free:
        ## Eliminar los adaptadores.
        ## Pasar la secuencia limpia a otro archivo
        for seq in lineas:
            seq_limpia = seq[14:]
            adapter_free.write(seq_limpia)

def fasta_generator(file_path,id , new_file = "results/new_fasta.fasta"):
  with open( file_path,'r') as dna:
        arch= dna.read()
  ## Se genera el nuevo archivo fasta
  fasta= open(new_file,"w")
  fasta.write(f">{id}\n")
  fasta.write(arch)
  fasta.close()
    
  
