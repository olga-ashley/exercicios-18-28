a=int(input('Insira o valor A: '))
b=int(input('Insira o valor B: '))
if a<=0 or b<=0:
    print('Não use um valor menor ou igual a 0.')
    quit()
if a>b:
    if a%b==0:
        a=str(a)
        b=str(b)
        print(a,'é maior que', b+ '.', a, 'é multiplo de', b +'.')
    else:
        a=str(a)
        b=str(b)
        print(a,'é maior que', b+ '.', a,'não é multiplo de', b +'.')
elif b>a:
    if b%a==0:
        a=str(a)
        b=str(b)
        print(b,'é maior que', a+ '.', b, 'é multiplo de', a +'.')
    else:
        a=str(a)
        b=str(b)
        print(b,'é maior que', a+ '.', b,'não é multiplo de', a +'.')
else:
    print('Os valores são iguais.')