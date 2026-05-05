def calcular_salario(brutos, horas):
    valor_hora = brutos / 220
    extra = valor_hora * 1.5 * horas
    inss = brutos * 0.11

    if brutos > 2000:
        vr = 150
    else:
        vr = 0

    liquido = brutos + extra - inss - vr

    return extra, inss, vr, liquido

def mostrar_extrato(nome, brutos,horas , extra, inss, vr, liquido):
    print(f"\n --- EXTRATO: {nome.upper()} --- ")
    print(f"Salário bruto: R$ {brutos:.2f}")
    print(f"Hora extra: R$ {extra:.2f} ({horas}h)")
    print(f"INSS: R$ {inss:.2f}")
    print(f"Vale Refeição: R$ {vr:.2f}")
    print(f"Salário liquido: R$ {liquido:.2f}")


def main():
    salarios = []

    try:
        n = int(input("Diga quantos funcionarios trabalharam: "))
    except:
        print("Entrada invalida")
        return
    
    for i in range(n):
        print(f"\n Funcionário {i+1}")

        nome = input("nome: ")

        try:
            brutos = float(input("Salário bruto: "))
            horas = float(input("Horas extras: "))
        except:
            print("Entrada invalida")
            continue
         
        extra, inss, vr, liquido = calcular_salario(brutos, horas)

        mostrar_extrato(nome, brutos, horas, extra, inss, vr, liquido)

        salarios.append(liquido)

    if len(salarios) > 0:
        print("\n--- RESUMO FINAL ---")
        print(f"Maior salário líquido: R$ {max(salarios):.2f}")
        print(f"Menor salário líquido: R$ {min(salarios):.2f}")
        print(f"Total da folha: R$ {sum(salarios):.2f}")
     


main()