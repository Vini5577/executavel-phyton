import os


def linha():
    print('-='*30)


def Menu():
    linha()
    print(f'{"MENU DE SELEÇÃO :":^60}')
    linha()
    print('1 - Abrir Word')
    print('2 - Abrir Excel')
    print('3 - Abrir Adobe Photoshop')
    print('4 - Abrir Adobre Premiere')
    print('5 - Sair do programa')
    linha()


def opção(n=0):
    if n == 1:
        path_dir = 'C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe'
    elif n == 2:
        path_dir = 'C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe'
    elif n == 3:
        path_dir = 'C:/Program Files/Adobe/Adobe Photoshop CC 2017/Photoshop.exe'
    elif n == 4:
        path_dir = 'C:/Program Files/Adobe/Adobe Premiere Pro CC 2018/Adobe Premiere Pro.exe'
    elif n == 5:
        print('')
    elif n != 1 or n != 2 or n != 3 or n != 4 or n != 5:
        print('\033[31mERRO! Digite novamente!\033[m')
    if n == 1 or n == 2 or n == 3 or n == 4:
        os.startfile(path_dir)
