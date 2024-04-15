### Subset Component

Dificuldade: Difícil

[Link para o enunciado completo](https://www.hackerrank.com/challenges/subset-component/problem)

Enunciado:

You are given an array with n 64-bit integers:d[0],d[1],...,d[n-1]. BIT(x, i) = (x >> i) & 1, where B(x,i) is the ith lower bit of x in binary form. If we regard every bit as a vertex of a graph G, there is an undirected edge between vertices i and j if there is a value k such that BIT(d[k], i) == 1 && BIT(d[k], j) == 1.

For every subset of the input array, how many connected components are there in that graph?

A connected component in a graph is a set of nodes that are accessible to each other via a path of edges. There may be multiple connected components in a graph.

Submissões:<br>
![image](https://github.com/projeto-de-algoritmos-2024/Grafos1-OnlineJudge/assets/88786065/b14d2e69-83c1-40bf-863a-dc0ef8421445)
