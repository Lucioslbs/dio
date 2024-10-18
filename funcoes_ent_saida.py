# Objetivo Geral
# Lendo valores com a função input (builtin)
nome = input("Informe o seu nome: ")
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))

if idade <= 20:
    print("Ainda é um adolescente!")
elif 20 < idade <= 30:
    print("Ainda está jovem!")
elif 30 < idade <= 50:
    print("Está ficando velho!")
else:
    print("A velhice chegou!")

if peso <= 30:
    print("Está magro, precisa de mais massa muscular!")
elif 30 < peso <= 60:
    print("Está mantendo seu peso!")
else:
    print("Está acima do peso!")

print(nome)
print(idade)
print(peso)
