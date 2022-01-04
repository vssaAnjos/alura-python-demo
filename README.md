# alura-python-demo
Alura | Curso Python 3 parte 1: Introdução à nova versão da linguagem

##  Tipagem de dados
- Função type() para imprimir o tipo da variavel. Ex:
pais=brasil
type(mes)
> class 'str''

* Linguagem dinâmica - tipagem dinâmica
* O tipo da variável vai ser igual ao valor do que ela recebe. 
Ex:
variavel = 1
Tipagem int
variavel = texto
Tipagem string

* Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:
idade = 12

* O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30
  
* Identação
4 espaços ou 1 tab
  
## Condição Se
Estrutura do IF e ELSE

- elif: aceita 
- else: não aceita condição, apenas a instrunção que será executada

If (condicao): 
    // faça tal coisa
elif(condicao):
    // faça tal coisa
else:
    // faça tal coisa
## Seguem todas as operadores de comparação:

    < - menor que
    > - maior que
    <= - menor ou igual a
    >= - maior ou igual a
    == - igual a
    != - diferente de

## Laço de repetição
Laço 'enquanto'

> while (condition):

## Laço for
```python 
for contador in range(1, 11):
    print(contador)
```

### Função range
> range(start, stop, [step])

Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:

## String interpolation
Saiba mais na Documentação: https://docs.python.org/3/library/string.html#formatexamples
uso de colchetes dentro de strings para formatar com váriaveis
Ex:
>     print("Tentativa {} de {}".format(rodada,total_de_tentativas))

Para utilizar outra ordem dos parametros
>     print("Tentativa {1} de {0}".format(1,10))
> Resultado: Tentativa {10} de {1}"

### Formatação de floats
Primeiro precisamos dizer para ela que estamos recebendo um valor do tipo float, passando :f dentro das chaves da string:

> print("R$ {}".format(1.59))
> R$ 1.59

Para formatar as casas decimais depois do ponto
> >>> print("R$ {:.2f}".format(1.59))
R$ 1.59
> >>> print("R$ {:.2f}".format(1.5))
R$ 1.50
>>> print("R$ {:.2f}".format(1234.50))
R$ 1234.50

##  Interpolação - Python 2 vs Python 3 
Python 3
> "{} {}".format(1, 2)

Python 2
> "%d %d" % (1, 2)

Mais exemplos, sempre comparando o Python 2 com Python 3, existem no link: https://pyformat.info/

* No Python 3.6+
A partir da versão 3.6 do Python, foi adicionado um novo recurso para realizar a interpolação de strings. Esse recurso é chamado de f-strings ou formatted string literals.
> nome = 'Maria'
> print(f'Meu nome é {nome}')
> Meu nome é Maria
* Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la
> nome = 'Maria'
> print(f'Meu nome é {nome.lower()}')
> Meu nome é maria

## Python builtin
Funções embutidas por padrão no Python
https://docs.python.org/3/library/functions.html

## Gerando números aleatórios
```python
import random
random.random()
0.6022965518496559
```
Arrendondando um número decimal 
```python
numero_random = random.random() * 100
numero_random
#resultado sem o round()
> 18.895629671768187
int(numero_random)
#resultado com convertendo para inteiro
> 18
round(numero_random)
#resultado com o round()
19
```

### Outras funções
Função `abs(valor)` usada para transformar o número em um valor absoluto e positivo.
```python
pontos_perdidos = abs(numero_secreto - chute)
```
O objetivo dessa função é retornar o número desconsiderando o seu sinal

### Float division
Repare que recebemos o valor float 1.5 como resposta. O operador / sempre traz um float, mesmo se não for necessário, por isso ele também é chamado de float division:
```python
>>>  3 / 2
1.5
```

## Criar Funções
>  Lembrando que é consenso usar a nomenclatura snake_case:

Definir:
```python
## arquivo.py
def funcao():
    // todo código aqui
```
Chamar:
```python
import arquivo
    arquivo.funcao()
```
> Uma função também pode receber parâmetros e retornar algum valor, por exemplo:
```python
def soma(a, b):
     return a + b
```
> A função soma recebe dois parâmetros (a e b) e retorna a soma. Ao chamar a função, podemos capturar o retorno:
```python
s = soma(3, 4) 
```

## Função main
> Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. 
> Então é preciso fazer if para verificar se ela está preenchida ou não:
```python
# adivinhacao.py

import random

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```
-- teste
