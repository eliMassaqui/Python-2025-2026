# Palavara reservada chamda def pra usar função!
# Nome da função, não pode ser igual a uma palabra reservada!
# A função pode ter parametros, como seus seus espaço primitivo que vária!
print("Sobre funções!")

# Parametro chamado nome:
def chamar(nome):
    return print(f"Olá Mundo, meu nome é {nome}")

#Duas formas diferentes de se chamar uma função!
chamar("Eli")
# Porque aqui aparece NONE pra quando printamos o retorno_2 a sós
retorno_2 = chamar(nome="Robot")
# print(retorno_2)