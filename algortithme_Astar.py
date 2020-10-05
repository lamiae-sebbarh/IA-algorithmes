

tree = {'S': ['A', 'B'],
         'A': ['S'],
         'B': ['S', 'C', 'D'],
         'C': ['B', 'E', 'F'],
         'D': ['B', 'G'],
         'E': ['C'],
         'F': ['C']
         }


def DFS(array):
    global visited_list, tree
   #visited_list contient les noueds visites 
    if set(tree[array[-1]]).issubset(visited_list):
   #renvoie True si tous les noeuds sont présents dans tree ,Sinon il renvoie False.     
        del array[-1]
        #supprimer le noeud precedets pour ne pas le repete dans la liste 
        return DFS(array)

    for item in tree[array[-1]]:
        if item in visited_list:
            continue
        visited_list.append(item)
        array.append(item)
        if item == 'G':
      #le G et le point ce qu'ont cherche une fois il est trouve on arrete la recherche       
            return array, visited_list
        else:
            return DFS(array)


if __name__ == '__main__':
    visited_list = ['S']
    solution, visited_nodes = DFS(['S'])
    print('Optimal solution: ' + str(solution))
    print('visited nodes: ' + str(visited_nodes))
