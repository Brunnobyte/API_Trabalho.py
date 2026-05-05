def obter_respostas():
    respostas = []
    for i in range(9):
        while True:
            try:
                valor = int(input(f"Resposta {i+1} (0-6): "))
                if 0 <= valor <= 6:
                    respostas.append(valor)
                    break
                else:
                    print("Digite um valor entre 0 e 6:")
            except:
                print("Entrada inválida")
    return respostas


def calcular_escores(respostas):
    exaustao = sum(respostas[0:3]) / 3
    despersonalizacao = sum(respostas[3:6]) / 3
    realizacao = sum(respostas[6:9]) / 3
    return exaustao, despersonalizacao, realizacao


def classificar_dimensao(valor, tipo):
    if tipo == "R":  # Realização (invertido)
        if valor <= 2:
            return "Baixa "
        elif valor <= 3.9:
            return "Moderada "
        else:
            return "Alta "
    else:
        if valor <= 2:
            return "Baixo "
        elif valor <= 3.9:
            return "Moderado "
        else:
            return "Alto "


def exibir_laudo(nome, ex, de, re):
    print(f"\n========== LAUDO: {nome.upper()} ==========")

    c1 = classificar_dimensao(ex, "N")
    c2 = classificar_dimensao(de, "N")
    c3 = classificar_dimensao(re, "R")

    print(f"Exaustão Emocional : {ex:.2f} → {c1}")
    print(f"Despersonalização : {de:.2f} → {c2}")
    print(f"Realização Pessoal : {re:.2f} → {c3}")

    criticos = 0
    if "Alto" in c1: criticos += 1
    if "Alto" in c2: criticos += 1
    if "Baixa" in c3: criticos += 1

    if criticos >= 2:
        print(f" Atenção: {criticos} dimensão(ões) em nível crítico.")
        print("Recomenda-se acompanhamento profissional.")


def main():
    nomes = []
    exaustoes = []
    realizacoes = []
    soma_burnout = 0
    total_respostas = 0

    try:
        n = int(input("Quantos respondentes? "))
    except:
        print("Entrada inválida!")
        return

    for i in range(n):
        print(f"\nRespondente {i+1}")
        nome = input("Nome: ")

        respostas = obter_respostas()
        ex, de, re = calcular_escores(respostas)

        exibir_laudo(nome, ex, de, re)

        nomes.append(nome)
        exaustoes.append(ex)
        realizacoes.append(re)

        soma_burnout += sum(respostas[0:6])
        total_respostas += 6

    if n > 0:
        maior_ex = max(exaustoes)
        menor_re = min(realizacoes)

        print("\n======= RESUMO DO ESTUDO =======")
        print("Respondentes:", n)
        print(f"Maior Exaustão: {nomes[exaustoes.index(maior_ex)].upper()} ({maior_ex:.2f})")
        print(f"Menor Realização: {nomes[realizacoes.index(menor_re)].upper()} ({menor_re:.2f})")
        print(f"Média Geral Burnout: {soma_burnout / total_respostas:.2f}")


main()
