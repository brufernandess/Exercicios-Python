# Exercício 05 - Alistamento Militar
from datetime import date
nasc=int(input('Em que ano você nasceu?: '))

ano= date.today().year
idade= ano - nasc

tempo= idade - 18

if idade == 18:
    print('Não perca tempo, já esta na hora de se alistar!')
elif idade < 18:
    print(f'Calma! Ainda nao chegou seu momento, ainda faltam {-tempo} anos')
else:
    print(f'Poxa, é uma pena mas já se passou {tempo} anos ')