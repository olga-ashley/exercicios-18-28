a=float(input('Insira o valor A.'))
b=float(input('Insira o valor B.'))

if a>b :
    d=str(a-b)
    print('A é maior que B, e a diferença é igual a '+ d +'.')
elif b>a :
    d=str(b-a)
    print('B é maior que A, e a diferença é igual a '+ d +'.')
else :
    print('A e B são iguais.')