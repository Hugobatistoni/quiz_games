import pycountry
from random import randint

#gera um pais aleatorio e print o resultado
paisAleatorio = list(pycountry.countries)[randint(1, 249)].name
    print(f'O pais aleatório selecionado foi: {paisAleatorio}')

### o que fiz de errado na linha abaixo ?
pais = input('Qual é o pais')
if pais == paisAleatorio :
    print('Você acertou')
else
    print('Você errou')
