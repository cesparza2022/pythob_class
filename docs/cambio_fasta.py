'''
NAME
    cambio_fasta
VERSION
    1.0
AUTHOR
  César Esparza
GITHUB
  https://github.com/cesparza2022/pythob_class
DESCRIPTION
  El codigo sirve para generar un archivo de DNA tipo FASTA a partir de uno raw

'''

##Obtener el archivo desde la ruta y sacar el contenido
arch = open("data/dna.txt","r")
contenido = arch.read()
arch.close()


## Se solicita el identificador de la secuencia 
id = input("ID de la secuencia ")

## Se genera el fasta 
arch_fasta = open("resultados/arreglo.fasta", "w")
arch_fasta.write(f">{id} \n{contenido}")
arch_fasta.close()

print("ya se guardo el archivo fasta en la carpeta de resultados")