import random

# Le um aruiivo txt e retorna uma lista com os dados

# Path: Driver/consumir_agents_txt.py
def ler_arquivo_txt():
    # Abre o arquivo txt
    try:
        arquivo = open("Driver/agents.txt", "r")
    except:
        print("Erro ao abrir o arquivo!")
        return False

    # Le o arquivo e armazena em uma lista
    lista = []
    for linha in arquivo:
        lista.append(linha.replace("\n", ""))
    arquivo.close()
    return lista

# Escolhe um agente aleatorio da lista
def escolher_agente():
    lista = ler_arquivo_txt()
    # Escolhe um agente aleatorio
    agente = random.choice(lista)
    return agente