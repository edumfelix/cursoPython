# Listas, Tuplas e Set

# Listas - São mutáveis
print('Listas')

fruits = ["apple", "cherry", "mango"]
print(fruits)
fruits.append("coconut")
print(fruits)
fruits.remove("cherry")
print(fruits)

# Tuplas - São imutáveis
print('\nTuplas')
cars = ("vw", "mercedes", "fiat")
print(cars)

# cars.append("toyota")
# print(cars)
# Apresentará erro pois tuplas são imutáveis
# Há duas formas de se alterar uma tupla:
# 1. Convertendo para list e depois revertendo para tupla.
# 2. Concatenando duas tuplas

# Set - Imutável e não ordenado
print("\nSets or Conjuntos")
maquina = {"Notebook", "PC", "Laptop"}

# Apresentará os itens de maquina de forma aleatória
for c in maquina:
    print(c)

# Se buscar por indice será apresentado um erro
# print(maquina[0])

# Podemos também fazer validação dessa forma:
print("Notebook" in maquina)
