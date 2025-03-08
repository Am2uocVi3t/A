from colorama import Fore, Style


def f01(message):
    print(Fore.GREEN + message + Style.RESET_ALL)


def f02(message):
    print(Fore.RED + message + Style.RESET_ALL)
    print("いいえ-")
