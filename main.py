import pycountry
from random import randint

#gera um pais aleatorio e print o resultado
paises = list(pycountry.countries)
indice_aleatorio = randint(0, len(paises) - 1)
paisAleatorio = paises[indice_aleatorio].name
print(f'O pais aleatório selecionado foi: {paisAleatorio}')

### o que fiz de errado na linha abaixo ?
pais = input('Qual é o pais')
if pais == paisAleatorio :
    print('Você acertou')
else:
    print('Você errou')
    print(f'O pais certo é: {paisAleatorio}')
