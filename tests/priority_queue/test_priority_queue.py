from ting_file_management.priority_queue import PriorityQueue
import pytest

value1 = {"qtd_linhas": 6}
value2 = {"qtd_linhas": 1}
value3 = {"qtd_linhas": 2}


def test_basic_priority_queueing():
    fila_com_prioridade = PriorityQueue()
    fila_com_prioridade.enqueue(value1)
    fila_com_prioridade.enqueue(value2)
    assert fila_com_prioridade.regular_priority._data == [value1]
    assert fila_com_prioridade.high_priority._data == [value2]
    fila_com_prioridade.dequeue()
    assert fila_com_prioridade.regular_priority._data == [value1]
    fila_com_prioridade.enqueue(value3)
    assert fila_com_prioridade.search(0) == value3
    with pytest.raises(IndexError):
        fila_com_prioridade.search(2)
