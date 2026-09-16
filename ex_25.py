HorasC=int(input('Horas (24h) do começo do jogo: '))
MinC=int(input('Minutos do começo do jogo: '))

HorasF=int(input('Horas (24h) do fim do jogo: '))
MinF=int(input('Minutos do fim do jogo: '))

if HorasF>24 or HorasF<0 or HorasC>24 or HorasC<0 or MinC>60 or MinC<0 or MinF>60 or MinF<0:
    print('Horário inválido.')
    exit()

if HorasF<HorasC:
    HorasF=HorasF+24

TempoMT=((HorasF*60)+MinF)-((HorasC*60)+MinC)

HorasTotal=TempoMT//60
MinTotal=TempoMT%60

print('O tempo total do jogo foi de',str(HorasTotal),'horas e',str(MinTotal),'minutos.')
