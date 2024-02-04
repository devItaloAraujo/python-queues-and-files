from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    linhas = txt_importer(path_file)

    value = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas,
    }
    if value not in instance._data:
        instance.enqueue(value)
        print(value, file=sys.stdout)


def remove(instance: Queue):
    if instance.is_empty():
        return print("Não há elementos", file=sys.stdout)
    removido = instance.dequeue()
    print(
        f"Arquivo {removido['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
