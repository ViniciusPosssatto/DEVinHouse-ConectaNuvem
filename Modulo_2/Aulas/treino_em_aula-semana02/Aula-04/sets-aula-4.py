# dois modos

set1 = { 1, 3, 5, 7 }

set2 = ({ 2, 3, 4, 5 })

set1.add(99) # adiciona apenas um elemento

set1.update([ 3, 45 ]) # adicionar mais de um elemento

ordenado = sorted(set1) # ordena os valores

set1.remove(33) # vai retornar erro se não tiver esse valor dentro

set1.discard(22) # descarta o item do parâmetro, mas não retorna erro se ele não existir

print(set1)
print(ordenado)

#--------------------------------------------------------

setA = {6, 9, 12, 24, 21}
setB = {9, 53, 12, 21, 30}

# Diferença 
# (pertencem A e não pertencem a B)
print("Diferença")
print(setA - setB)
print(setA.difference(setB))

# Diferença Simétrica 
# (itens que pertencem aos dois conjuntos e que não estão na interseção)
print("Diferença Simétrica")
print(setA ^ setB)
print(setA.symmetric_difference(setB))


# União 
# (união dos dois conjuntos)
print("União")
print(setA | setB)
print(setA.union(setB))

# Interseção 
# (pertencem ao conjunto A e B)
print("Interseção")
print(setA & setB)
print(setA.intersection(setB))