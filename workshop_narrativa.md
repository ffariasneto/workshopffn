# Variáveis e Condicionais
Variáveis são "palavras chave" que armazenam valores, como números, textos ou listas, para serem reutilizados no programa. Elas têm um nome e um valor atribuído.

Condicionais permitem que o programa tome decisões de acordo com ocondições específicas. Usam as estruturas if, elif(else if) e else. Quando a condição definida em if é verdadeira, o bloco de código correspondente é executado; se for falsa, o programa pode verificar outras condições com elif ou executar uma ação alternativa com else.

# Como criar uma função no Python
é um bloco de código reutilizável que realiza uma tarefa específica. Você define uma função usando a palavra-chave def, seguida pelo nome da função e parênteses.
```
def saudacao():
    print("Olá, bem-vindo!")

def saudacao(nome):
    print(f"Olá, {nome}, bem-vindo!")

saudacao("Ana)
```



Para chamar um função, basta escrever o nome da função seguido de parênteses no lugar onde deseja que ela seja executada. Se a função tiver parâmetros, você coloca os valores dentro dos parênteses.

Combinar funções e condicionais permite criar códigos mais dinâmicos e reutilizáveis. Você pode usar condicionais dentro de uma função para que ela tome decisões com base nos valores dos parâmetros ou outras condições.

```
def verifica_idade(idada):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

print(verifica_idade(idade))
```

