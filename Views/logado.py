from tkinter import Tk, Label, Entry, Button
import json
from Driver.invokeChrome import DriverBot
from time import sleep
from Controllers.criarConta import criar_conta

#importar thread
from threading import Thread



def salvar_dados():
    # Obter os valores dos campos de entrada
    api_proxy = api_proxy_entry.get()
    link_reset_api = link_reset_api_entry.get()
    senha_contas = senha_contas_entry.get()

    # Cria um objeto com os dados
    dados = {
        "API_PROXY": api_proxy,
        "Link Reset API": link_reset_api,
        "Senha para contas": senha_contas
    }

    # Salva os dados em um arquivo json
    try:
        with open("BancoDeDados/dados.json", "w") as arquivo:
            json.dump(dados, arquivo)
        message_label.config(text="Dados salvos com sucesso!")
    except Exception as e:
        message_label.config(text=f"Erro ao salvar os dados: {str(e)}")
    


def carregar_dados():
    try:
        with open("BancoDeDados/dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except:
        return None


dados_carregados = carregar_dados()












def iniciar_criacao():
    # Lógica para iniciar a criação usando os dados fornecidos
    api_proxy = api_proxy_entry.get()
    link_reset_api = link_reset_api_entry.get()
    senha_contas = senha_contas_entry.get()

    # Criar uma thread para executar o criar_conta
    thread = Thread(target=criar_conta, args=(senha_contas,))
    thread.start()

    




def tela_logado():
    global message_label, api_proxy_entry, link_reset_api_entry, senha_contas_entry
    # Criar a janela principal
    root = Tk()
    root.title("Usuário Logado")

    width = 300
    height = 220
    root.geometry(f"{width}x{height}")

    # Label e Entry para API_PROXY
    api_proxy_label = Label(root, text="API_PROXY")
    api_proxy_label.pack()
    api_proxy_entry = Entry(root)
    api_proxy_entry.pack()

    # Label e Entry para Link Reset API
    link_reset_api_label = Label(root, text="Link Reset API")
    link_reset_api_label.pack()
    link_reset_api_entry = Entry(root)
    link_reset_api_entry.pack()

    # Label e Entry para marcadorPasta
    senha_contas_label = Label(root, text="Qual pasta deseja abrir?")
    senha_contas_label.pack()
    senha_contas_entry = Entry(root)
    senha_contas_entry.pack()

    # Botão para salvar os dados
    salvar_button = Button(root, text="Salvar", command=salvar_dados)
    salvar_button.pack()

    # Botão para iniciar a criação
    iniciar_button = Button(root, text="Abrir Perfil", command=iniciar_criacao)
    iniciar_button.pack()

    # Label para exibir mensagens
    message_label = Label(root, text="")
    message_label.pack()

    # Verificar se os dados foram carregados com sucesso
    if dados_carregados is not None:
        api_proxy = dados_carregados.get("API_PROXY")
        link_reset_api = dados_carregados.get("Link Reset API")
        senha_contas = dados_carregados.get("Senha para contas")

        # Inserir os valores nos campos de entrada
        api_proxy_entry.insert(0, api_proxy)
        link_reset_api_entry.insert(0, link_reset_api)
        senha_contas_entry.insert(0, senha_contas)

    # Iniciar o loop do Tkinter


    root.mainloop()


