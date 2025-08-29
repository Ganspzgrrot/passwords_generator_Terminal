import random as r

from colorama import Back, Style, Fore, init

init()

 

def erzeugung(lenght, chars):

    passwort = ''

    for i in range(lenght):

        passwort += r.choice(chars)

    return passwort

 

digits = '1234567890'

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

punctuation = '!#$%&*+-=?@^_'

 

chars = ''

 

a = Fore.RED + '██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n''█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███\n''█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███\n''█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███\n''█░░▄▀░░██░░▄▀░░███░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███\n''█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███\n''█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███\n''█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███\n''█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████\n''█░░▄▀░░██░░▄▀░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█\n''█░░▄▀░░██░░▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█\n''█░░░░░░██░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█\n''██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████' + Style.RESET_ALL

print(a)

 

counter_passwords = int(input('Количество паролей: '))

lenght_password = int(input('Длина пароля: '))

 

print(Fore.MAGENTA + '┍┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┓' + Style.RESET_ALL)

inpt1 = Fore.GREEN + 'Включать' + Style.RESET_ALL + ' ли' + Fore.YELLOW + ' цифры' + Style.RESET_ALL + ' ' + Back.GREEN + " 1234567890" + Style.RESET_ALL + '?' + Back.GREEN + '(д = да ' + Style.RESET_ALL + Back.RED + "н = нет" + ")\n" + Style.RESET_ALL + Fore.MAGENTA + '┕┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷--:' + Style.RESET_ALL

all_numbers = input(inpt1)

 

print(Fore.MAGENTA + '┍┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┓' + Style.RESET_ALL)

inpt2 = Fore.GREEN + 'Включать' + Style.RESET_ALL + ' ли' + Fore.YELLOW + ' прописные буквы' + Style.RESET_ALL + ' ' + Back.GREEN + " ABCDEFGHIJKLMNOPQRSTUVWXYZ" + Style.RESET_ALL + '?' + Back.GREEN + '(д = да ' + Style.RESET_ALL + Back.RED + "н = нет" + ")\n" + Style.RESET_ALL + Fore.MAGENTA + '┕┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷--:' + Style.RESET_ALL

on_uppercase = input(inpt2)

 

print(Fore.MAGENTA + '┍┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┓' + Style.RESET_ALL)

inpt3 = Fore.GREEN + 'Включать' + Style.RESET_ALL + ' ли' + Fore.YELLOW + ' строчные буквы' + Style.RESET_ALL + ' ' + Back.GREEN + " abcdefghijklmnopqrstuvwxyz" + Style.RESET_ALL + '?' + Back.GREEN + '(д = да ' + Style.RESET_ALL + Back.RED + "н = нет" + ")\n" + Style.RESET_ALL + Fore.MAGENTA + '┕┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷--:' + Style.RESET_ALL

on_lowercase = input(inpt3)

 

print(Fore.MAGENTA + '┍┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┯┓' + Style.RESET_ALL)

inpt4 = Fore.GREEN + 'Включать' + Style.RESET_ALL + ' ли' + Fore.YELLOW + ' символы' + Style.RESET_ALL + ' ' + Back.GREEN + " !#$%&*+-=?@^_" + Style.RESET_ALL + '?' + Back.GREEN + '(д = да ' + Style.RESET_ALL + Back.RED + "н = нет" + ")\n" + Style.RESET_ALL + Fore.MAGENTA + '┕┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷--:' + Style.RESET_ALL

on_symbols = input(inpt4)


 

off_neodn_symbols = input(Fore.RED + 'Исключать ' + Style.RESET_ALL + 'ли ' + Fore.YELLOW + 'неоднозначные символы ' + Style.RESET_ALL + Fore.RED + "il1Lo0O" + Style.RESET_ALL + '? ' + Back.GREEN + '(д = да ' + Style.RESET_ALL + Back.RED + "н = нет" + ")\n" + Style.RESET_ALL + Fore.MAGENTA + '┕┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷┷--:' + Style.RESET_ALL)

 

if all_numbers.lower() in ['да', 'д', 'l', 'lf']:

    chars += digits

if on_uppercase.lower() in ['да', 'д', 'l', 'lf']:

    chars += uppercase_letters

if on_lowercase.lower() in ['да', 'д', 'l', 'lf']:

    chars += lowercase_letters

if on_symbols.lower() in ['да', 'д', 'l', 'lf']:

    chars += punctuation

if off_neodn_symbols.lower() in ['да', 'д', 'l', 'lf']:

    for i in 'il1Lo0O':

        chars = chars.replace(i, '')

       

print(Fore.RED + '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' + Style.RESET_ALL)        

for kreedmoor in range(counter_passwords):

    print(Fore.YELLOW + '|‑‒–—――――――――: ' + Style.RESET_ALL + erzeugung(lenght_password, chars))

   

print(Fore.RED + '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒' + Style.RESET_ALL)    

sdfg = input('Нажмите на энтер для выхода из проги: ')      