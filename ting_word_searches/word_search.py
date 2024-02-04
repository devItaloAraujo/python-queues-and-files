from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []
    for item in instance._data:
        information = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index in range(len(item["linhas_do_arquivo"])):
            if word.lower() in item["linhas_do_arquivo"][index].lower():
                information["ocorrencias"].append({"linha": index + 1})
        if len(information["ocorrencias"]) > 0:
            result.append(information)
    return result


def search_by_word(word, instance):
    result = []
    for item in instance._data:
        information = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index in range(len(item["linhas_do_arquivo"])):
            if word.lower() in item["linhas_do_arquivo"][index].lower():
                information["ocorrencias"].append(
                    {
                        "linha": index + 1,
                        "conteudo": item["linhas_do_arquivo"][index],
                    }
                )
        if len(information["ocorrencias"]) > 0:
            result.append(information)
    return result
