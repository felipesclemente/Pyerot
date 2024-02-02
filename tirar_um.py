import random
import get_arcana

arcana = get_arcana.monta_lista()


def jogar():
    print("Tiragem de uma carta")
    carta = random.choice(arcana)
    invertida = random.choice([True, False])
    if invertida:
        print("A sua carta é: {}, invertida.".format(carta))
    else:
        print("A sua carta é: {}, na vertical.".format(carta))


if __name__ == "__main__":
    jogar()
