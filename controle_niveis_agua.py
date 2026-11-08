from colorama import init, Fore, Style

init()

# Situações organizadas do nível mais baixo ao mais alto.
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    return Style.RESET_ALL


# Simulação das mudanças no nível de água.
for nivel_atual in range(1, 6):
    situacao = niveis[nivel_atual - 1]
    cor = definir_cor(nivel_atual)

    print(
        f"{cor}Nível {nivel_atual}: {situacao}"
        f"{Style.RESET_ALL}"
    )