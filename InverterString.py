
#  Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Solicita entrada do usuário
string = input("Digite uma string: ")

# Inicializa a string invertida
string_invertida = ""

# Itera por cada caractere da string, do fim para o início
for i in range(len(string)-1, -1, -1):
    # Adiciona o caractere à string invertida
    string_invertida += string[i]

# Exibe a string invertida
print("A string invertida é:", string_invertida)