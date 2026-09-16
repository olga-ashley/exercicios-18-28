numA=float(input('Insira o valor A: '))
numB=float(input('Insira o valor B: '))
numC=float(input('insira o valor C: '))
numX=float(input('Insira o valor X: '))
if numA>numB or numB>numC:
    print('A, B e C devem ser sequenciais.')
    quit()
if numX<numA:
    print(str(numX)+',',str(numA)+',',str(numB)+',',str(numC)+'.')
elif numX<numB:
    print(str(numA)+',',str(numX)+',',str(numB)+',',str(numC)+'.')
elif numX<numC:
    print(str(numA)+',',str(numB)+',',str(numX)+',',str(numC)+'.')
else:
    print(str(numA)+',',str(numB)+',',str(numC)+',',str(numX)+'.')