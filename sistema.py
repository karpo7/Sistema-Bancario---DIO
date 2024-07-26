menu = """
---- MENU ----

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

Digite a letra do que deseja realizar: 
"""

saldo = 0
LIMITE_SAQUES = 3
limite = 500
numero_saques = 0
extrato = ""

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("\nQual valor você deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("\nQual valor você deseja sacar: "))
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor > limite:
            print("Não é possível fazer o saque desse valor! (Saque Máx: R$ 500).")
        elif saldo < valor:
            print("Você não possui saldo suficiente.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
