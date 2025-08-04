nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")


print("Os dados inseridos foram: ")

# Ótimas formatações de texto:

print(
    f"\tNome: {nome}\n"
    f"\tIdade: {idade}\n" # Quebras de linhas.
    f"\tAltura: {float(altura):.2f}" #Tratamento de flutuante especialemte pra arredondar!
)