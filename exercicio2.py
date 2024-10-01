num = int(input("Digite um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    next_value = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_value)

if num in fibonacci:
    print(f"O número {num} faz parte da sequência de Fibonacci.")
else:
    print(f"O número {num} não faz parte da sequência de Fibonacci.")