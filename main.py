primer_numero = int(input())
segundo_numero = int(input())

def mcd(primero, segundo):
    
    while segundo != 0:
        
        primero, segundo = segundo, primero % primero
        
    return primero
    
maximo_comun = mcd(primer_numero,segundo_numero)

print(f"el MCD de {primer_numero}  y {segundo_numero} es {minimo_comun}")
