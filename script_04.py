"""
Listas em PYTHON

É um tipo de dado onde podemos armazenar em um conjunto de dados, inclusive outras listas.

São objetos indexáveis, modificáveis, iteráveis e que permitem valores repetidos.

"""

if __name__ == "__main__":

    # Criando listas de duas formas:
    lista1 = [1, 2, 3, 4, 5]
    lista2 = list("Python")

    print(lista1)
    print(lista2)

    # Como listas são objetos indexáveis, podemos acessar qualquer item da lista pelo seu índice.
    # Atenção, o índice em uma lista começa pelo valor 0.
    # Acessamos o item pelo índice passando o índice dentro de colchetes.

    lista3 = ["Abacaxi", "Manga", "Melancia", "Limao"]
    print(lista3[2])

    # A partir dos índices também conseguimos alterar um valor na lista.
    lista3[3] = "Abacate"
    print(lista3)

    # Para inserir itens na nossa lista, podemos utilizar os métodos:

    # append() -> Que insere um novo item ao final da lista.
    lista3.append("Goiaba")
    print(lista3)

    # insert()  -> Insere um novo item na lista no índice especificado
    # Insere "Pitanga" no índice 2 da lista
    lista3.insert(2, "Pitanga")
    print(lista3)

    # extend()  -> Ele insere os itens de um outro iterável no final da lista
    lista4 = ["Batata", "Tomate", "Alface", "Brócolis"]
    lista3.extend(lista4)
    print(lista3)

