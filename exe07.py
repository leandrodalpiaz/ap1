print ('Atividade 07')
 
nome = input('Qual seu nome? ')
salario = float(input('Qual o seu salário atualmente? '))
 
if salario >= 0 and salario <= 400:
    sc = salario + (salario * 0.15)
    print (f'{nome}, seu salário terá um aumento de 15%, sendo corrigido para R${sc}!')
elif salario >= 400.01 and salario <= 700:
    sc = salario + (salario * 0.12)
    print (f'{nome}, seu salário terá um aumento de 12%, sendo corrigido para R${sc}!')
elif salario >= 700.01 and salario <= 1000:
    sc = salario + (salario * 0.10)
    print (f'{nome}, seu salário terá um aumento de 10%, sendo corrigido para R${sc}!')
elif salario >= 1000.01 and salario <= 1800:
    sc = salario + (salario * 0.07)
    print (f'{nome}, seu salário terá um aumento de 7%, sendo corrigido para R${sc}!')
elif salario >= 1800.01 and salario <= 2500:
    sc = salario + (salario * 0.04)
    print (f'{nome}, seu salário terá um aumento de 4%, sendo corrigido para R${sc}!')
else:
    print (f'{nome}, você não terá nenhum aumento.')
