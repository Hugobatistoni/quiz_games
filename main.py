import pycountry
from random import randint

paisAleatorio = list(pycountry.countries)[randint(1, 249)].name
print(f'O pais aleatório selecionado foi: {paisAleatorio}')
