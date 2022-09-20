print ('Atividade 03')
 
indice = float(input('Qual é o índice de poluição medido no momento? '))
 
if indice >= 0.3 and indice < 0.4:
    print (f'Devido ao indice {indice} de poluição, o primeiro grupo de empresas está intimidade a suspender as atividades.')
elif indice >= 0.4 and indice < 0.5:
    print (f'Devido ao indice {indice} de poluição, o primeiro grupo e o segundo grupo de empresas está intimidade a suspender as atividades.')
elif indice >= 0.5:
    print (f'Devido ao indice {indice} de poluição, todos os grupos de empresas serão notificados e terão que suspender as atividades.')
else:
    print (f'O ídice {indice} de poluição é aceitável!')
