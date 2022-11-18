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


