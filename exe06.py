print ('Atividade 06')
 
n1 = float(input('Quanto você tirou na NI? '))
n2 = float(input('Quanto você tirou na N2? '))
n3 = float(input('Quanto você tirou na N3? '))
 
ma = (n1 + n2 + n3) / 3
 
if ma >= 9.0:
    print (f'A média de aproveitamento entre as notas {n1}, {n2} e {n3} é {ma}, você tirou um A, parabéns você foi APROVADO!')
elif ma >= 7.5 and ma < 9.0:
    print (f'A média de aproveitamento entre as notas {n1}, {n2} e {n3} é {ma}, você tirou um B, parabéns você foi APROVADO!')
elif ma >= 6.0 and ma < 7.5:
    print (f'A média de aproveitamento entre as notas {n1}, {n2} e {n3} é {ma}, você tirou um C, parabéns você foi APROVADO!')
elif ma >= 4.0 and ma < 6.0:
    print (f'A média de aproveitamento entre as notas {n1}, {n2} e {n3} é {ma}, você tirou um D, infelizmente você foi REPROVADO!')
else:
    print (f'A média de aproveitamento entre as notas {n1}, {n2} e {n3} é {ma}, você tirou um E, infelizmente você foi REPROVADO!')
