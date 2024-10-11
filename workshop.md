
# Condicionais: If, Else, Elif
- O que são: Condicionais permitem ao programa tomar decisões. Dependendo da condição, o programa executa
um código ou outro.
- Sintaxe básica:
```
numb1 = int(input("Digite um número: "))

if numb1 > 87:
    print(f"O número {numb1} é maior que 87.")
else:
    print(f"O número {numb1} é menor que 87.")

if numb1 % 2 == 0:
    print("é par")
else:
    print("é ímpar")
```
# Introdução a Funções
- São blocos de código que realizam uma tarefa específica.
## Por que usar:
- Reutilizar código;
- Organizar melhor o programa;
- Tornar o código mais legível.
### Estrutura básica
```
def nome_da_função():
    # Código aqui
```
```
def boas_vindas():
    print("Seja muito bem-vindo(a) ao curso de Data Science - Infinity School!")

boas_vindas()
```
```
def soma(numb1, numb2):
    return numb1 + numb2

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print(soma(n1, n2))
```
## Introdução a loops (For e While)
- Loops: Repetindo ações
São usados para repetir ações várias vezes.
### Tipos de loops
### for
Usado quando sabemos o número de repetições
### while
Usado qunado queremos repetir algo até uma condição ser satisfeita
```
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} é par!")
    else:
        print(f"{i} é ímpar!")
```
# Série de desafios!
## Desafio 1: Números Positivos e Negativos
Objetivo: Criar um código que verifica se um número é positivo, negativo ou zero.
```
numb = int(input("Digite um número: "))
if numb > 0:
    print(f"{numb} é positivo!")
elif numb < 0:
    print(f"{numb} é negativo!")
else:
    print("O número é zero")
```


