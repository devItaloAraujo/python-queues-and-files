from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self._data[0]
        else:
            return None

    def __str__(self):
        str_queue = ""
        for index in range(len(self._data)):
            str_queue += str(self._data[index]) + " "
            if index < len(self._data) - 1:
                str_queue += "<- "

        return "FILA: |Inicio| " + str_queue + "|Fim|"

    def search(self, value):
        if not 0 <= value < len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")

        return self._data[value]
