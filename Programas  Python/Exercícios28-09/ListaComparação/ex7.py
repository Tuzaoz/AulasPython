n1 = int(input('Digite o Primeiro Número \n'))
n2 = int(input('Digite o Segundo Número \n'))
n3 = int(input('Digite o Terceiro Número \n'))
maiornumero = n2
menornumero = n2

if n1 >= n2:
    maiornumero = n1
elif n1 <= n2:
    menornumero = n1
if n3 >= maiornumero:
    maiornumero = n3
elif n3 <= menornumero:
    menornumero = n3

print('O Maior número é ',maiornumero)
print('O Menor número é', menornumero)