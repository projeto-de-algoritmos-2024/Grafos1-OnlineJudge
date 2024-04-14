from collections import deque  # Importa a classe deque do módulo collections
from typing import List  # Importa o tipo de dados List do módulo typing

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)  # Obtém o número de nós no grafo
        INF = float('inf')  # Define o valor infinito como o maior número possível

        # Função BFS para encontrar o caminho mais curto
        def bfs(start):
            queue = deque([(start, 1 << start, 0)])  # Inicializa a fila com o nó inicial, bitmask e distância
            visited = set([(start, 1 << start)])  # Inicializa um conjunto de nós visitados e suas bitmasks
            
            while queue:  # Enquanto a fila não estiver vazia
                node, bitmask, distance = queue.popleft()  # Obtém o próximo nó, bitmask e distância
                
                if bitmask == (1 << N) - 1:  # Se todos os nós foram visitados
                    return distance  # Retorna a distância
                
                for neighbor in graph[node]:  # Para cada vizinho do nó atual
                    new_bitmask = bitmask | (1 << neighbor)  # Atualiza a bitmask
                    if (neighbor, new_bitmask) not in visited:  # Se o vizinho ainda não foi visitado
                        queue.append((neighbor, new_bitmask, distance + 1))  # Adiciona o vizinho à fila
                        visited.add((neighbor, new_bitmask))  # Adiciona o vizinho aos visitados
        
        min_path_length = INF  # Inicializa o comprimento mínimo do caminho como infinito
        
        # Executa a busca BFS a partir de cada nó e atualiza o comprimento mínimo do caminho
        for start_node in range(N):
            min_path_length = min(min_path_length, bfs(start_node))
        
        return min_path_length  # Retorna o comprimento mínimo do caminho
    
# Cria uma instância da classe Solution
sol = Solution()

# Define os exemplos de grafos fornecidos
graph1 = [[1,2,3],[0],[0],[0]]
graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]

# Imprime o comprimento mínimo do caminho para cada exemplo de grafo
print(sol.shortestPathLength(graph1))  # Saída esperada: 4
print(sol.shortestPathLength(graph2))  # Saída esperada: 4
