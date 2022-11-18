"""
Laço for de repetição

O laço for é usado para iterar (acessar sequencialmente item a item) sobre sequências de itens

list - listas
dict - dicionários
tuple - tuplas
set - sets (conjuntos)

Além desses tipos de sequências, também podemos utilizar o laço for em strings

Calcular o quadrado de uma lista de números

Dentro do laço for podemos utilizar dois comandos:

    -break: interrompe imediatamente a execução do laço
    -continue: ignora o resto do bloco e volta a linha

Também é possível ser utilizado o else ao lado do for, para executar um bloco após o laço for terminar.

"""

# Leia os itens da lista até encontrar a palavra "Nenhuma". Encontrando, sair do loop.

if __name__ == "__main__":
    lista_palavras = [
        "Abacaxi", "Manga", "Nenhuma", "Maçã", "Uva"
    ]

    for palavra in lista_palavras:
        if palavra == "Nenhuma":
            break
        print(palavra)

    print("-"*33)

    lista_numeros = [
        5, 10, 14, 7, 8
    ]
    soma = 0

    for numero in lista_numeros:
        if numero % 2 == 1:
            continue

        soma += numero
    else:
        print("Todos os itens foram processados")

    print(f"Soma: {soma}")

    # Utilizando for com a função geradora range()
    for numero in range(1, 100, 5):
        print(numero)
