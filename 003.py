"""
Cálculo de média das provas

Trabalhando com operadores aritiméticos, lógicos e de comparação

O sistema recebe 3 notas, e calcula a média aritimética dessas notas

Se a média for menor do que 5, o sistema mostra uma mensagem de aluno REPROVADO
Se a média for maior ou igual a 5 e menor do que 7, o sistema mostra uma mensagem de aluno em recuperação
Se a média for maior do que 7, o sistema mostra uma mensagem de aluno APROVADO

Na linha 27, também pode ser utilizada dessa forma: # elif media >= 5 and media < 7:

E na linha 31 pode mudar o if para else: e pular para a próxima linha de descrição

"""

if __name__ == "__main__":
    nota_1 = float(input("Informe a primeira nota: "))
    nota_2 = float(input("Informe a segunda nota: "))
    nota_3 = float(input("Informe a terceira nota: "))

    media = (nota_1+nota_2+nota_3) / 3

    print(f"A média geral é: {media:.2f}")

    if media < 5:
        print('aluno REPROVADO')
    elif 5 <= media < 7:
        print('aluno em recuperação')
    if media > 7:
        print('aluno APROVADO')