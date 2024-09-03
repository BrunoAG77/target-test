import json

def percentuais(faturamento_mensal):
    faturamento_total = sum(faturamento_mensal.values())
    percentual = {}
    for estado, valor in faturamento_mensal.items():
        percent = (valor/faturamento_total) * 100
        percentual[estado] = percent
        print(f"{estado}: {percent:.2f}%")
    return percentual

def load():
    with open('dados.json','r') as file:
        dados = json.load(file)
    return dados

def calculo_faturamento(faturamento_daily):
    faturamento = [dia['valor'] for dia in faturamento_daily if dia['valor'] > 0]
    menor = min(faturamento)
    maior = max(faturamento)
    media = sum(faturamento)/len(faturamento)
    dias_acima = sum(1 for valor in faturamento if valor > media)
    return menor, maior, dias_acima

def fibonacci(n):
    fib = [0,1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

#1
i = 13
soma = 0
k = 0

while k < i:
    k = k + 1
    soma = soma + k

print(soma)

#2
number = int(input("\nDigite o termo para verificar se pertence à sequência de Fibonacci: \n"))
fib = fibonacci(number)
if number in fib:
    print("\nO numero",number,"pertence à sequência de Fibonacci")
else:
    print("\nO numero",number,"não pertence à sequência de Fibonacci")

#3
faturamento_daily = load()
menor, maior, dias_acima = calculo_faturamento(faturamento_daily)
print(f"\nMenor valor de faturamento: {menor:.2f}\nMaior valor de faturamento: {maior:.2f}\nNúmero de dias acima da média: {dias_acima:.2f}")

#4
faturamento_mensal = {"SP":67836.43, "RJ":36678.66, "MG":29229.88, "ES":27165.48, "Outros":19849.53}
print("\n",percentuais(faturamento_mensal))

#5
string = str(input("\nDigite uma frase: "))
gnirts = string[::-1]
print(gnirts)
    
