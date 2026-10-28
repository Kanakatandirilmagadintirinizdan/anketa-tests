import os
from registry import Registry

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "anketa.txt")
OK_FILE = os.path.join(BASE_DIR, "ok.txt")
ERRORS_FILE = os.path.join(BASE_DIR, "errors.txt")

def main():
    reg = Registry()
    if not reg.load(INPUT_FILE):
        print(f"Файл {INPUT_FILE} не найден!")
        return

    reg.print_table()
    reg.print_stats()
    reg.save(OK_FILE, ERRORS_FILE)

if __name__ == "__main__":
    main()