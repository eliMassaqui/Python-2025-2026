## Chamar uma função:

def diz_ola(nome):
    return f"Olá Mundo, meu nome é {nome}!"


retotorno_1 = diz_ola("Adriano")
retotorno_2 = diz_ola(nome="João")
resultado = retotorno_1, retotorno_2

global printando
printando = "12345"

for n in printando:
    print(resultado)
    print(retotorno_1)
    print(retotorno_2)
    print(printando)
    print(n)