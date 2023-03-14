# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele 
# calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def fibonacci(n):
    """Calcula a sequência de Fibonacci até o número n."""
    fib = [0, 1]
    while fib[-1] < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

def pertence_fibonacci(n):
    """Verifica se o número n pertence à sequência de Fibonacci."""
    fib = fibonacci(n)
    if n in fib:
        print(f"{n} pertence à sequência de Fibonacci!")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

# Exemplo de uso:
while True:
    numero = int(input("Digite um número inteiro: "))
    print(fibonacci(numero))
    pertence_fibonacci(numero)