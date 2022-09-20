c_aluno = input('Qual o código do Aluno? ')
 
nota_01 = float(input('I - De 0 a 10 qual foi a sua nota? '))
nota_02 = float(input('II - De 0 a 10 qual foi a sua nota? '))
nota_03 = float(input('III - De 0 a 10 qual foi a sua nota? '))
 
 
maior_nota = max (nota_01, nota_02, nota_03)
 
nota_4 = maior_nota * 4
 
notas_menores = (nota_01 + nota_02 + nota_03) - maior_nota
 
notas_3 = notas_menores * 3
 
media = (nota_4 + notas_3) / (4 + 3 + 3)
 
if media >= 7:
    print(f'O aluno de nº {c_aluno} com notas entre {nota_01}, {nota_02} e {nota_03} obtendo uma média de {media}, sendo assim está APROVADO!')
else:
    print(f'O aluno de nº {c_aluno} com notas entre {nota_01}, {nota_02} e {nota_03} obtendo uma média de {media}, sendo assim está REPROVADO!')
