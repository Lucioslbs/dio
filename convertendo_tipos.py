# Convertendo tipos variaveis

preco = 10
idade = 28
print(preco, idade)

preco = int(preco)
print(preco / 2) # retorna valor flutuante
print(preco // 2) # retorna valor int

texto = f"idade {idade} preco {preco}"
print(texto)

preco1 = "10.50"
idade1 = "28"
print(float(preco1))
