nucleotidos = ["A", "T","C","G"]
reversos = {"A":"T", "T":"A","C": "G","G":"C"}

def reverso(arreglo):
  return"".join( reversos[nuc] for  nuc in arreglo)

arreglo = input("ingresa la secuencia: ") 

print (f"5'{arreglo} 3'")  
print(f"   {''.join(['|' for nuc in range(len(arreglo))])}") 
print(f"3' {reverso(arreglo)} 5'")

