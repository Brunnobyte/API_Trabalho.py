def main():
    menu =  '''
    >>> Urna <<<
    1. - Votar
    2. - Ver Resultado
    3. - Encerrar
    ----
    0 - Sair > '''

    votos = [0, 0, 0, 0, 0, 0]

    def votar(votos):
        voto = int(input("Digite o seu voto de (0-5):"))
        
        if 0 <= voto <=5:
            votos[voto] += 1
        else:
            print("Voto inválido")

    def mostrar_resultado(votos):
        total_validos = sum(votos[1:5])

        print("\nResultado:")
        print("Válidos:", total_validos)
        print("Brancos:", votos[0])
        print("Nulos:", votos[5])

        if total_validos > 0:
            for i in range(1, 5):
                porcentagem = (votos[i] / total_validos) * 100
                print(f"Candidato {i}: {porcentagem:.2f}%")

            candidatos = votos[1:5]
            maior = max(candidatos)
            vencedores = [index + 1 for index, valor in enumerate(candidatos) if valor == maior]

            print("Vencedor(es):", vencedores)

            if maior / total_validos <= 0.5:
                print("Haverá segundo turno!")
        else:
            print("Sem votos válidos.")

    while True:
        print(menu)
        opcao = int(input("Escolha: "))
        
        if opcao == 1:
            votar(votos)
        elif opcao == 2:
            mostrar_resultado(votos)
        elif opcao == 3:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


main()