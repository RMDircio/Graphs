"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # self.vertices = {
        #     # manually add the vertices via dictionary/set
        #     # Adjacency List
        #     1: {2},
        #     2: {3, 4},
        #     3: {5},
        #     4: {6, 7},
        #     5: {3},
        #     6: {3},
        #     7: {1, 6}
        # }
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # check to make sure the vertices do not exist
        if vertex_id not in self.vertices:
            # if not in set 
            # create a new key with vertex_id & set to an empty set - no edges
            self.vertices[vertex_id] =  set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # both vertex 1 and vertex 2 do not already exist
        if v1 in self.vertices and v2 in self.vertices:
            # get vertex 1, then add vertex 2 to the edges set
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # get vertex via id to return neighbors
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        BREADTH-FIRST TRAVERSAL
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # use the util.py for queue code :D
        # create an empty queue and enqueue the starting_vertex
        # create empty set to track visited vertices

        # while the queue is NOT empty:

            # get current vertex (dequeue from queue)
            
            # check if current vertex has not been visited:
                # print the current vertex
                # mark the current vertex as visited
                    # add current vertex to a visited_set
                # queue up all current vertex's neighbors

    def dft(self, starting_vertex):
        """
        DEPTH-FIRST TRAVERSAL
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use the util.py for stack code :D
        # create an empty stack and add the starting_vertex
        # create empty set to track visited vertices

        # while the stack is NOT empty:

            # get current vertex (pop from stack)
            
            # check if current vertex has not been visited:
                # print the current vertex
                # mark the current vertex as visited
                    # add current vertex to a visited_set
                # push up all current vertex's neighbors

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        BREADTH-FIRST SEARCH (stop when I find something or can
        I get from one place to another)
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # use the util.py for stack and queue code :D
        # create an empty queue and enqueue PATH to the starting_vertex
        # create empty set to track visited vertices

        # while the queue is NOT empty:

            # get current vertex PATH (dequeue from queue)
            # set current vertex to the last element of PATH
            
            # check if current vertex has not been visited:
                # Check if current vertex is destination
                    # if true - stop and return vertex

                # mark the current vertex as visited
                    # add current vertex to a visited_set
                # queue up all current vertex's neighbors

                # queue up NEW PATHS with each neighbor
                    # take current PATH
                    # append neighbor
                    # queue up NEW PATH

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # this graph is in 'objectives --> breadth-first-search --> img --> bfs-visit-order
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices) # this does :D

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
