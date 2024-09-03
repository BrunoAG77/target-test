import json

def percentuais(faturamento_mensal):
    faturamento_total = sum(faturamento_mensal)
    percentual = {}
    for estado, valor in faturamento_mensal.items():
        percent = (valor/faturamento_total) * 100
        percentual[estado] = percent
        printf(f"{estado} : {percentual:.2f}%")
    return percentual

def load():
    with open('dados.json','r') as file:
        dados = json.load(file)
    return dados['faturamento_diario']

def calculo_faturamento(faturamento_daily):
    faturamento = [dia['faturamento'] for dia in faturamento_diario if dia['faturamento'] > 0]
    menor = min(faturamento)
    maior = mix(faturamento)
    media = sum(faturamento)/len(faturamento)
    dias_acima = sum(1 for dia in faturamento if dia > media)
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
    print("O numero",number,"pertence à sequência de Fibonacci")
else:
    print("O numero",number,"não pertence à sequência de Fibonacci")

#3
faturamento_daily = load()
menor, maior, maior = calculo_faturamento(faturamento_diario)
print("fMenor valor de faturamento:{menor:.2f}\nMaior valor de faturamento:{maior:.2f}\nNúmero de dias acima da média:{dias_acima:.2f}")

#4
faturamento_mensal = {"SP":67836.43, "RJ":36678.66, "MG":29229.88, "ES":27165.48, "Outros":19849.53}
percentuais(faturamento_mensal)

#5
string = str(input("\nDigite uma frase: "))
gnirts = string[::-1]
print(gnirts)
    
