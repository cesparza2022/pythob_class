'''
NAME
	validacion_fasta
    
VERSION
    1.1
    
AUTHOR
    César Esparza

GITHUB
  https://github.com/cesparza2022/pythob_class
    
DESCRIPTION
    Convierte el archivo a formato fasta y valida la secuencia
        
CATEGORY
	Genomic Sequence

ARGUMENTS
        none
    
'''
ruta = input("ingrese la ruta del archivo: ")
nucs = ["A", "C", "G", "T"]

try:
    with open( ruta,'r') as dna:
        arrays = dna.readlines()
    

except IOError as io_error:
    print(f"No se encuentra el archivo {io_error} \n")


else:
     
    with open("resultados\dna_seq_fasta.fasta", 'w') as fasta:

   ## Se separan en id y secuencia los renglones
   ## Se valida la secuencia
   ## Se escribe en formato fasta 
        for line in arrays:
            id_o_seq = line.split("   ")
            id = id_o_seq[0]
            seq = id_o_seq[1] 
            seq = seq.upper()
            for nuc in seq:
                if nuc not in nucs:
                    seq = seq.replace(nuc,"")
            fasta.write(f"> {id}\n{seq}")


    print("El archivo 'dna_seq_fasta.fasta' con el output  se encuentra en el directorio de resultados")