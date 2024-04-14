# OnlineJudge

**Número da Lista**: [847]<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 21/1039519  |  João Manoel Barreto Neto |
| 21/1039789  |  Guilherme Soares Rocha |

## Sobre 
Neste repositório se encontra questões resolvidas do juiz online "Leetcode" sobre grafos, com o intuito de aplicar os conhecimentos obtidos na primeira etapa da disciplina de Projeto de Algoritmo. 

## Questões

### #847 - Menor caminho visitando todos os nós

Enunciado:

Você tem um gráfico conectado e não direcionado de n nós rotulados de 0 a (n - 1). Você recebe uma matriz graph onde em graph[i] está uma lista de todos os nós conectados ao nó i por uma aresta.

Retorne o comprimento do caminho mais curto que visita cada nó . Você pode iniciar e parar em qualquer nó, pode revisitar os nós várias vezes e pode reutilizar arestas.

Link para enunciado completo com exemplos: https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/

Resolução:
![Leetcode_847]("Grafos1-OnlineJudge\imagens\codigo_comentado_847.png")

Accepted:
![Accepted_847]("Grafos1-OnlineJudge\imagens\accepted_847.png")

Submissões:
![Sub_847]("Grafos1-OnlineJudge\imagens\codigo_accepted_847.png")

![Subs_847]("Grafos1-OnlineJudge\imagens\submissoes_847.png")

Obs: As duas últimas submissões são as mesmas, porém a última está com o código comentado

### #2872 - Máximo número de componentes K-divisíveis
## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

### Subset Component

Enunciado:
Você recebe um vetor com n inteiros de 64 bits: d[0], d[1], ..., d[n-1].
BIT(x, i) = (x >> i) & 1, onde B(x,i) é o i-ésimo bit inferior de x na forma binária. Se considerarmos cada bit como um vértice de um grafo G, existe uma aresta não direcionada entre os vértices i e j se houver um valor k tal que BIT(d[k], i) == 1 && BIT(d[k] , j) == 1.
Para cada subconjunto da matriz de entrada, quantos componentes conectados existem nesse grafo?
Um componente conectado em um grafo é um conjunto de nós acessíveis entre si por meio de um caminho de arestas. Pode haver vários componentes conectados em um grafo.

Link para o problema: https://www.hackerrank.com/challenges/subset-component/problem

Submissões:
![image](https://github.com/projeto-de-algoritmos-2024/Grafos1-OnlineJudge/assets/88786065/b14d2e69-83c1-40bf-863a-dc0ef8421445)


## Instalação 
**Linguagem**: Python<br>

## Uso 
Necessário ter o python instalado
