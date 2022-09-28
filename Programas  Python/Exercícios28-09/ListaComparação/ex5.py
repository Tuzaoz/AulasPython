nota1 = eval(input('Digite a primeira nota \n'))
nota2 = eval(input('Digite a segunda nota \n'))
media = int((nota1 + nota2)/2)
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7 and media<10:
    print('Aluno Aprovado')
if media <7:
    print('Reprovado')