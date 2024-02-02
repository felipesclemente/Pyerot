def monta_lista():
    with open("arcana_pt.txt", encoding='utf-8') as arquivo:
        arcana = []
        for linha in arquivo:
            linha = linha.strip()
            arcana.append(linha)
    return arcana
