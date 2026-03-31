import json

def carregar_dados(nome_arquivo):
    """Lê o arquivo JSON e retorna a lista de dicionários."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio, retorna lista vazia
        return []

def salvar_dados(nome_arquivo, lista_dicionarios):
    """Salva a lista de dicionários no formato JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # indent=4 deixa o arquivo legível para humanos
            json.dump(lista_dicionarios, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return False

dados = "cadastros.json"
lista = carregar_dados(dados)
