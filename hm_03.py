import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(directory, prefix=''):
    try:
        p = Path(directory)
        if not p.exists():
            print(f"{Fore.RED}Помилка: Вказаний шлях не існує.")
            return
        if not p.is_dir():
            print(f"{Fore.RED}Помилка: Це не директорія.")
            return
        
        for item in p.iterdir():
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                print_directory_structure(item, prefix + '    ')
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")
    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py <шлях_до_директорії>")
    else:
        print_directory_structure(sys.argv[1])
