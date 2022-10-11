from Menu import *
from time import sleep
import os

while True:
    Menu()
    op = int(input('Selecione uma das opções: '))
    opção(op)
    if op == 5:
        print('Encerrando o programa...')
        sleep(1)
        break
    os.system("cls")
