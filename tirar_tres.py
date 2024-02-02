import random
import get_arcana

arcana = get_arcana.monta_lista()


def jogar():
    print("Tiragem de três cartas")
    carta = random.sample(arcana, k=3)
    index = 0
    posicao = ["primeira", "segunda", "terceira"]
    for _ in carta:  # O underscore é usado como variável quando não precisa ser acessado em outros lugares
        invertida = random.choice([True, False])
        if invertida:
            print("A {} carta é: {}, invertida.".format(posicao[index], carta[index]))
        else:
            print("A {} carta é: {}, na vertical.".format(posicao[index], carta[index]))
        index += 1


if __name__ == "__main__":
    jogar()
