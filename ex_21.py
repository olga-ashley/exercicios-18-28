nota=['0','0','0','0','0']
for i in range(1, 5):
    nota[i]=float(input('Digite a nota '+ str(i) +'.'))

media=(nota[1]+nota[2]+nota[3]+nota[4])/4

if media>=6:
    print('Aprovado')
elif media>=3:
    print('Exame')
else:
    print('Retido')