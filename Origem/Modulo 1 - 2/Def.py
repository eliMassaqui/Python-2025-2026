# Palavra reservada chamada def para criar função!
# Nome da função não pode ser igual a uma palavra reservada!
# A função pode ter parâmetros, que são variáveis locais da função.
print("Sobre funções!")

# Parâmetro chamado nome:
def chamar(nome):
    return f"Olá Mundo, meu nome é {nome}"

# Duas formas diferentes de se chamar uma função!
print(chamar("Eli"))
retorno_2 = chamar(nome="Robot")
print(retorno_2)