"""
Entrada e saída padrão em Python

Utilizamos 2 funções:
    print() -> Imprime um texto na tela
    input() -> Recebe uma informação pelo teclado

Conversor de reais para dólares

A função input sempre retorna uma string, independentemente do valor informado no terminal.

Para operações matemáticas, é necessário converter o valor de entrada (String) em um valor numérico.

Nesse caso, utilizamos as funções built-in int() e/ou float()

O "f" no início da string significa f-string. Utilizando f-strings, conseguimos inserir facilmente expressões python
dentro de string.

O .format() ao final, depois das aspas,tem a mesma função do "f-string". Ficando dessa forma:
print(f"O valor convertido é igual a: ".format(valor_convertido))

O :.2f limita o valor que aparece em 2 casas após a vírgula nos casos de float.

"""

if __name__ == "__main__":
    valor_em_reais = float(input("Insira o valor em reais: "))
    cotacao_do_dolar = float(input("Insira a cotação atual do dólar: "))

    valor_convertido = valor_em_reais * cotacao_do_dolar

    print(f"O valor convertido é igual a: {valor_convertido:.2f}")
