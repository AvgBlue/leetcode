# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []


from typing import Dict, List, Optional


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        clone_dict: Dict[Node, Node] = {}

        def runner(node: Optional[Node]) -> Optional[Node]:
            nonlocal clone_dict
            new_neighbors: List[Node] = []
            new_node = Node(node.val, new_neighbors)
            clone_dict[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in clone_dict:
                    new_neighbors.append(clone_dict[neighbor])
                else:
                    new_neighbor = runner(neighbor)
                    new_neighbors.append(new_neighbor)

            return new_node

        return runner(node)


if __name__ == "__main__":
    # Example usage:
    # Create a sample graph: 1 -- 2
    #                        |    |
    #                        4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned = solution.cloneGraph(node1)

    # Simple check: print values and neighbors of the cloned graph
    def print_graph(node, visited):
        if node in visited:
            return
        visited.add(node)
        print(f"Node {node.val}, Neighbors: {[n.val for n in node.neighbors]}")
        for neighbor in node.neighbors:
            print_graph(neighbor, visited)

    print_graph(cloned, set())
