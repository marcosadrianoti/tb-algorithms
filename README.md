# Projeto Python Algorithms! :robot:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Resolver problemas e otimizar algoritmos desenvolvendo a capacidade de implementar soluções.
  * Verificar se eu era capaz de:
    * Exercitar lógica.
    * Interpretar problemas.
    * Interpretar um código legado.
    * Otimizar a resolução de problemas.
    * Resolver problemas/Otimizar algoritmos sob pressão.
    * Identificar a complecidade do algorítimo.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  * Número de estudantes estudando no mesmo horário (_Algoritmo de busca_)
    * Retornar, para uma entrada específica, a quantidade de estudantes presentes.
    * Retornar `None` se em `permanence_period` houver alguma entrada inválida.
    * Retornar `None` se `target_time` recebe um valor vazio.
    * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n)` - _complexidade assintótica linear_
  * Criptografia de inversões (_Testes_)
    * Implementar adequadamente o teste para a função `encrypt_message`.
  * Palíndromos (_Recursividade_)
    * Retornar `True` se a palavra passada por parâmetro for um palíndromo.
    * Retornar `False` se a palavra passada por parâmetro não for um palíndromo.
    * Retornar `False` se nenhuma palavra for passada por parâmetro.
  * Anagramas (_Algoritmo de ordenação_)
    * Retornar `True` se as palavras passadas forem anagramas.
    * Retornar `False` se as palavras passadas por parâmetro não forem anagramas.
    * Retornar `false` se alguma das palavras passadas por parâmetro for uma string vazia.
    * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n log n)` - _complexidade assintótica linearítmica_
    * Retornar `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas.
  * Requisitos Bônus:
    * Encontrando números repetidos (_Algoritmo de busca_)
      * Retornar o número repetido se a função receber como parâmetro uma lista com números repetidos.
      * Retornar `False` se a função não receber nenhum parâmetro.
      * Retornar `False` se a função receber, como parâmetro, uma string.
      * Retornar `False` se a função receber, como parâmetro, uma lista sem números repetidos.
      * Retornar `False` se a função receber, como parâmetro, apenas um valor.
      * Retornar `False` se a função receber, como parâmetro, um número negativo.
      * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n log n)` - _complexidade assintótica linearítmica_
    * Palíndromos (_Iteratividade_)
      * Retornar `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa.
      * Retornar `False` se a palavra passada como parâmetro não for um palíndromo, executando uma função iterativa.
      * Retornar `False` se nenhuma palavra for passada como parâmetro, executando uma função iterativa.
      * A função deverá, por meio de análise empírica, se comportar como no máximo `O(n)` - _complexidade assintótica linear_
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-algorithms.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-algorithms
```

Instale as dependências executando:

```bash
npm install
```

Com o Docker instalado em sua máquina, execute:

```bash
npm run compose:up
```

Execute a aplicação:

```bash
npm run start
```

Para exercutar os teste:

```bash
npm run test
```
