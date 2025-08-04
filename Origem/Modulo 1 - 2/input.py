# nome = input("Digite o seu nome: ")
# print(nome)

#Basicamente o funcionamento do computador como:

# Entrada De Dados:

#Chamando input com mensagens predefinidas pra usuário.
numero = input("Digite o number: ")
expoente = input("Digite o expoente: ")

# Preocessamento De Dados:

# Calculando, mas pra evitar erro dde que: não pode calcular sequencia de valores não-int
# Que nesse caso chamamos dentro da função int que fez a transformção por baixo dos panos.
resultadoExpoente = int(numero) * int(expoente)

# Saída De Dados:

# Agora fazemos o tratamento, agora na função de interpolação de strings
# Não esquecer do f antes da string
print(f"O resultado de {numero} elevado a {expoente} é igual: {resultadoExpoente}")