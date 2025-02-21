import sys
print("------------------------")
print("-------BEM-VINDO--------")
print("------------------------")
print("opcao 1 -------- SACAR")
print("opcao 2 -------- DEPOSITAR")
print("opcao 3 -------- SAIR")
opcao = int(input("escolha uma opcao: "))

def sacar():
    saldo = 500
    dinheiro_a_sacar = float(input("o quanto voce quer sacar?: "))
    saldo = saldo - dinheiro_a_sacar
    print(saldo)

def depositar():
    saldo = 500
    dinheiro_a_depositar = float(input("o quanto voce quer depositar?: "))
    saldo = saldo + dinheiro_a_depositar
    print(saldo)
    
while opcao != 3:

    if opcao == 1:
        sacar()
    if opcao == 2:
        depositar()
    if opcao == 3:
        sys.exit()

    print("opcao 1 -------- SACAR")
    print("opcao 2 -------- DEPOSITAR")
    print("opcao 3 -------- SAIR")
    opcao = int(input("escolha uma opcao: "))

