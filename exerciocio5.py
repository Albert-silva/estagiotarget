string = input("Digite um string: ")


string_invertida = ""

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]


print("O string invertido é:", string_invertida)