nVoltas=int(input('Digite o número de voltas: '))
extCircuito=int(input('Digite a extensão do circuito em metros: '))
tDuracao=float(input('Digite o tempo de duração em minutos: '))

if nVoltas<=0 or extCircuito<=0 or tDuracao<=0:
    print('Não use valores menores ou iguais a zero.')
    quit()

velM= ((extCircuito/1000)*nVoltas) / (tDuracao/60)
print('A velocidade média é de',str(velM),'Km por hora.')