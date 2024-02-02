import tirar_um
import tirar_tres

print("Bem vindo ao Pyerot, cartomante digital de Tarot")


def escolhe_tiragem():
    print("(1) Tiragem de uma carta")
    print("(3) Tiragem de três cartas")
    escolha = int(input("Escolha a sua opção: "))
    if escolha == 1:
        tirar_um.jogar()
    elif escolha == 3:
        tirar_tres.jogar()
    else:
        print("Escolha inválida, digite apenas 1 ou 3")
        escolhe_tiragem()


if __name__ == "__main__":
    escolhe_tiragem()
