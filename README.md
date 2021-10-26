# alura-python-demo
Alura - curso Python 3

# Tipagem de dados
- Função type() para imprimir o tipo da variavel. Ex:
pais=brasil
type(mes)
>> class 'str''

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
> nome = 'Matheus'
> print(f'Meu nome é {nome}')
> Meu nome é Matheus
* Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la
> nome = 'Matheus'
> print(f'Meu nome é {nome.lower()}')
> Meu nome é matheus