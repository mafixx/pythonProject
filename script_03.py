"""
Laço While

O laço While é utilizado quando é preciso repetir um bloco de comando, enquanto uma condição for verdadeira.

"""

from random import randint

if __name__ == "__main__":

    # opcao = "CONTINUAR"
    # lista_valores = []
    # soma = 0
    #
    # while opcao == "CONTINUAR":
    #     valor = input("Informe um valor ('SAIR' para finalizar)")
    #
    #     if valor.isalpha() and valor.upper() == "SAIR":
    #         opcao = valor.upper()
    #         continue
    #
    #     elif valor.isdecimal():
    #         soma += int(valor)

    soma = 0
    contador = 0

    while soma < 100:
        # Incremetado o valor da variável soma com o valor randômico de 1 a 10
        soma += randint(1, 10)  # = soma = soma + randint(1, 10)
        contador += 1

    print(f"O programa levou {contador} iterações para chegar ao valor {soma}.")
