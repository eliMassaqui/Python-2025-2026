# nome = input("Digite o seu nome: ")
# print(nome)

#Chamando input com mensagens predefinidas pra usuário.
numero = input("Digite o number: ")
expoente = input("Digite o expoente: ")

# Calculando, mas pra evitar erro dde que: não pode calcular sequencia de valores não-int
# Que nesse caso chamamos dentro da função int que fez a transformção por baixo dos panos.
resultadoExpoente = int(numero) ** int(expoente)
print(resultadoExpoente)