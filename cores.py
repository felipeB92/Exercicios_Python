class Estilo:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    VERMELHO = "\033[31m"
    VERMELHONEG = "\033[1;31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

    # Cores de fundo (Background)
    FUNDO_VERMELHO = "\033[41m"
    FUNDO_VERDE = "\033[42m"
    FUNDO_AZUL = "\033[44m"


def colorir(texto, cor,Linha=False):
    """Retorna o texto formatado com a cor desejada e reseta ao final."""
    if Linha:
        print (f"{cor}{texto}\033[m", end="")
    else:
        print(f"{cor}{texto}\033[m")