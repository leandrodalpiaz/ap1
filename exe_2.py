print ('Atividade 02')

i  = int(input('Digite um número de 1 a 3: '))
a = int(input('I - Digite qualquer valor: '))
b = int(input('II - Digite qualquer valor: '))
c = int(input('III - Digite qualquer valor: '))
result = [a, b, c]

if i == 1:
    result.sort()
    print(f'Ordem Crescente: {result}')
    result.sort(reverse=True)
elif i == 2:
    result.sort(reverse=True)
    print(f'Ordem Decrescente: {result}')
elif i == 3:
    if (a > b) and (a > c):
        print(f'Maior no meio: {b}, {a}, {c}')
    if (b > a) and (b > c):
        print(f'Maior no meio: {a}, {b}, {c}')
    if (c > a) and (c > b):
        print(f'Maior no meio:{a},{c},{b}')
