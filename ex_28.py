vendaMen=int(input('Digite a venda mensal do produto: '))
precoAtual=float(input('Digite o preço atual dele: '))
precoNovo=float(0)

if vendaMen<=0 or precoAtual<=0:
    print('Não use valores menores ou iguais a 0.')
    quit()

if vendaMen<500 and precoAtual<30:
    precoNovo=precoAtual+(precoAtual*(1/10))
elif vendaMen>=500 and vendaMen<1000 and precoAtual>=30 and precoAtual<80:
    precoNovo=precoAtual+(precoAtual*(3/20))
elif vendaMen>=1000 and precoAtual>=80:
    precoNovo=precoAtual-(precoAtual*(1/20))

if precoNovo>0:
    print('O preço novo é de',precoNovo,'reais.')
else:
    print('Não há mudança no preço.')
