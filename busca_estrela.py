# algoritmo de busca de estrela para IA

import heapq  # Importa o módulo heapq para usar a fila de prioridade

class Node:
    """
    Representa um nó no grid.
    """
    def __init__(self, pos, parent=None):
        self.pos = pos  # Posição (x, y) do nó no grid
        self.parent = parent  # Nó pai (usado para rastrear o caminho)
        self.g = 0  # Custo do caminho do início até este nó
        self.h = 0  # Heurística (estimativa do custo deste nó até o destino)
        self.f = 0  # Custo total (g + h)

    def __lt__(self, other):
        # Comparação para a fila de prioridade (ordena por f)
        return self.f < other.f

def a_star(grid, start, end):
    """
    Encontra o caminho mais curto entre start e end em um grid usando A*.

    Args:
        grid: Uma lista de listas representando o grid (0 para livre, 1 para obstáculo).
        start: Posição inicial (x, y).
        end: Posição final (x, y).

    Returns:
        Uma lista de posições representando o caminho, ou None se não houver caminho.
    """
    
    # Inicializa nós de início e fim
    start_node = Node(start)  # Cria o nó inicial
    end_node = Node(end)  # Cria o nó final

    # Listas aberta e fechada
    open_list = []  # Lista de nós a serem explorados (fila de prioridade)
    closed_list = set()  # Conjunto de nós já explorados

    # Adiciona o nó inicial à lista aberta
    heapq.heappush(open_list, start_node)  # Adiciona o nó inicial à fila de prioridade

    # Loop principal
    while open_list:  # Enquanto houver nós na lista aberta
        current_node = heapq.heappop(open_list)  # Pega o nó com menor f da lista aberta
        closed_list.add(current_node.pos)  # Adiciona o nó atual à lista fechada

        # Verifica se o destino foi alcançado
        if current_node.pos == end_node.pos:  # Se o nó atual é o destino
            path = []  # Inicializa a lista do caminho
            while current_node:  # Reconstrói o caminho do destino ao início
                path.append(current_node.pos)  # Adiciona a posição do nó ao caminho
                current_node = current_node.parent  # Move para o nó pai
            return path[::-1]  # Retorna o caminho invertido (do início ao destino)

        # Explora os vizinhos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Loop pelos 4 vizinhos (cima, baixo, esquerda, direita)
            neighbor_pos = (current_node.pos[0] + dx, current_node.pos[1] + dy)  # Calcula a posição do vizinho

            # Verifica se o vizinho é válido
            if (0 <= neighbor_pos[0] < len(grid) and  # Verifica se está dentro dos limites do grid
                0 <= neighbor_pos[1] < len(grid[0]) and  # Verifica se está dentro dos limites do grid
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and  # Verifica se é um espaço livre (não um obstáculo)
                neighbor_pos not in closed_list):  # Verifica se não foi explorado antes

                neighbor_node = Node(neighbor_pos, current_node)  # Cria o nó vizinho
                neighbor_node.g = current_node.g + 1  # Calcula o custo g do vizinho
                neighbor_node.h = abs(neighbor_pos[0] - end_node.pos[0]) + abs(neighbor_pos[1] - end_node.pos[1])  # Calcula a heurística h (Manhattan)
                neighbor_node.f = neighbor_node.g + neighbor_node.h  # Calcula o custo total f do vizinho

                # Adiciona ou atualiza o vizinho na lista aberta
                if neighbor_node not in open_list:  # Se o vizinho não está na lista aberta
                    heapq.heappush(open_list, neighbor_node)  # Adiciona à lista aberta
                # Se já está na lista aberta e o novo caminho é melhor, atualize o custo

    # Se a lista aberta ficar vazia, não há caminho
    return None  # Retorna None se não encontrar um caminho

if __name__ == "__main__":
    # Definição do grid (0 = livre, 1 = obstáculo)
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    # Posição inicial e final
    start = (0, 0)  # Posição inicial
    end = (3, 3)  # Posição final

    # Chama a função a_star e imprime o resultado
    path = a_star(grid, start, end)
    if path:
        print("Caminho encontrado:", path)
    else:
        print("Nenhum caminho encontrado.")
