from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, prev_node, divs, adj, values, k):
            node_val = values[node] # Inicializa a variável node_val com o valor do nó atual.

            # Percorre os vizinhos do nó atual na lista de adjacência
            for neighbor in adj[node]: 
                if neighbor != prev_node: # Verifica se o vizinho atual não é o nó anteriormente visitado, para evitar ciclos na busca.
                    node_val += dfs(neighbor, node, divs, adj, values, k) # Chama recursivamente a função dfs para explorar o vizinho atual e atualiza node_val com o retorno da chamada recursiva.

            if node_val % k == 0: # Verifica se a soma dos valores dos nós do componente atual é divisível por k.
                divs[0] += 1 # Se a soma dos valores for divisível por k, incrementa o número de divisões válidas.
                return 0

            return node_val

        adj = [[] for _ in range(n)] # Inicializa a lista de adjacência adj como uma lista vazia para cada nó na árvore.
        for edge in edges:
            adj[edge[0]].append(edge[1]) # Adiciona o segundo nó da aresta como um vizinho do primeiro nó na lista de adjacência.
            adj[edge[1]].append(edge[0]) # Adiciona o primeiro nó da aresta como um vizinho do segundo nó na lista de adjacência.

        # roda a dfs para o primeiro nó
        divs = [0]  # Inicializa a lista de divisoes com um elemento 0, que será usado para contar o número de divisões válidas.
        dfs(0, -1, divs, adj, values, k) #  Chama a função dfs para iniciar a busca em profundidade a partir do nó 0.
        return divs[0] # Retorna o número de divisões válidas encontradas.

# Teste dos exemplos fornecidos
sol = Solution()

n1 = 5
edges1 = [[0,2],[1,2],[1,3],[2,4]]
values1 = [1,8,1,4,4]
k1 = 6
print(sol.maxKDivisibleComponents(n1, edges1, values1, k1))  # Saída esperada: 2

n2 = 7
edges2 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values2 = [3,0,6,1,5,2,1]
k2 = 3
print(sol.maxKDivisibleComponents(n2, edges2, values2, k2))  # Saída esperada: 3