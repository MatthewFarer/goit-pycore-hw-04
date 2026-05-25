import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def print_directory_structure(path, indent=""):
    try:
        for item in path.iterdir():

            # if that is a directory
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}")

                # recursively print the structure of the subdirectory
                print_directory_structure(item, indent + "    ")

            # if that is a file
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")

    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу до {path}")


def main():

    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        return

    # get path from command line argument
    directory_path = Path(sys.argv[1])

    # check if the path exists
    if not directory_path.exists():
        print(Fore.RED + "Вказаний шлях не існує.")
        return

    # check if the path is a directory
    if not directory_path.is_dir():
        print(Fore.RED + "Вказаний шлях не є директорією.")
        return

    print(Fore.YELLOW + directory_path.name)

    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()