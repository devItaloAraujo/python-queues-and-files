import sys


def txt_importer(path_file):

    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    # raise error if file does not exist
    try:
        with open(path_file, "r") as file:
            result = file.read().split("\n")
            return result
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
