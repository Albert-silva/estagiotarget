import json


with open('dados.json') as file:
    faturamento_diario = json.load(file)

valores = [i["valor"] for i in faturamento_diario]

minimo = min(valores)

maximo = max(valores)

media = sum (valores) / len (valores)

acima_da_media = 0
for v in valores:
    if v > media:
        acima_da_media += 1 


print("Menor faturamento diário:", minimo)
print("Maior faturamento diário:", maximo)
print("Número de dias com faturamento acima da média mensal:", acima_da_media)