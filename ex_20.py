cA=float(input('Insira o valor de A.'))
cB=float(input('Insira o valor de B.'))
cC=float(input('Insira o valor de C.'))

delta=float((cB**2)-(4*cA*cC))
if delta==0:
    raiz1=-cB/(2*cA)
    print('A única raiz é igual a '+ raiz1 +'.')
elif delta>0:
    raiz1=(-cB-(delta**0.5)) / (2*cA)
    raiz2=(-cB+(delta**0.5)) / (2*cA)
    print('As raízes são iguais a '+ str(raiz1) +' e '+ str(raiz2) +'.')
else:
    print('Esta equação não possui raízes reais.')
