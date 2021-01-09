'''                 Artem's Lecture  - CSPT11
            https://www.youtube.com/watch?v=jyOzMMBr_qE&feature=youtu.be
'''
class Graph:
    def __init__(self):
        self.verticies = {}

    # add verticies
    def add_vertex(self, vertex_id):
        # dictonary[key] = value as a set
        self.verticies[vertex_id] = set() # this is empty if there are no neighbors

    # add edges
    def add_edges(self, v1, v2): # (from, to)
        # if both verticies are in the graph
        if v1 in self.verticies and v2 in self.verticies:
            # make the connection
            # verticies of v1(key) add to v2(value)
            self.verticies[v1].add(v2)
        else:
            print('ERROR: Vertex Not Found.')

    # get a representation of all the neighbors
    def get_neighbors(self, vertex_id):
        # return the value set for the key
        return self.verticies[vertex_id]

    # traversing the graph - Queue
    def bft(self, starting_vertex_id):
        ''' Breadth First Traveral looks at all
        not visited neighbors before following a path.
        BFT always have Setup Phase, a Queue, Visited Set, a While Loop,
        Check if Visited Phase, Reason for Traversal Part, Get Neighbors,
        Add Neighbors to Queue.
        '''
        # neet to keep track of current visited nodes + neighbors 
        # that are up next to be visited

        # make empty queue - add starting vertex
        # keeps track of next_to_visit_verticies
        queue = [] # just using a list here - first in, first out - append and delete from start
        queue.append(starting_vertex_id)

        # make an empty set - 
        # keeps track of visited_verticies
        visited_verticies = set()

        # while the queue is not empty
        while len(queue) > 0: 
            # dequeue (pop) a vertex off the front queue
            current_vertex = queue.pop(0)

            # if the vertex has not been seen before
            if current_vertex not in visited_verticies:
                # we want to print the visited vertex
                print(current_vertex)
                # add the vertex to our visited set
                visited_verticies.add(current_vertex)
                # add all new neighbors to the queue with for loop + function
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)


 # traversing the graph - Stack
    def dtf(self, starting_vertex_id):
        ''' Depth First Traveral looks at all
        not visited neighbors on a single path till the end.
       
        '''
        # neet to keep track of current visited nodes + neighbors 
        # that are up next to be visited

        # make empty stack - add starting vertex
        # keeps track of next_to_visit_verticies
        stack = [] # just using a list here - first in, last out - append and delete from end
        stack.append(starting_vertex_id)

        # make an empty set - 
        # keeps track of visited_verticies
        visited_verticies = set()

        # while the stack is not empty
        while len(stack) > 0: 
            # pop a vertex off the end of the stack
            current_vertex = stack.pop()

            # if the vertex has not been seen before
            if current_vertex not in visited_verticies:
                # we want to print the visited vertex
                print(current_vertex)
                # add the vertex to our visited set
                visited_verticies.add(current_vertex)
                # add all new neighbors to the stack with for loop + function
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)





    # searching the graph - finds the SHOREST PATH TO TARGET
    def bfs(self, starting_vertex_id, target_vertex_id):
        '''
        This algorithm does Breadth First Search unitl the goal vertex
        is found. Returns an array of vertex IDs that are part of the PATH.
        '''
        # create an empty queue and ADD a PATH to starting vertex
        # in other words - add array [1] to the queue
        queue = [[starting_vertex_id]]

        # create a visited set of verticies
        visited_verticies = set()

        # while queue is NOT empty
        while len(queue) > 0:
            # dequeue the current PATH from the front of the queue
            current_path = queue.pop(0)

            # get the current vertex to analyze from the end of the PATH
            # use the vertex at the END of the PATH array
            current_vertex = current_path[-1]

            # if vertex has not been visited
            if current_vertex not in visited_verticies:
                # add vertex to visited list
                visited_verticies.add(current_vertex)

                # check if current vertex is the target vertex
                if current_vertex == target_vertex_id:
                    # found the vertex and the PATH to it
                    # return the PATH
                    return current_path

                # for each neighbor of the current vertex
                for neighbor in self.get_neighbors(current_vertex):
                    # add the PATH to that neighbor to the queue
                    # COPY  the current PATH
                    current_path_copy = list(current_path)
                    # add neightbor to the new path
                    current_path_copy.append(neighbor)
                    # add the whole PATH to the queue
                    queue.append(current_path_copy)
        
        # return None if no PATH exists
        return None

# set up graph
our_graph = Graph()

# add all verticies
our_graph.add_vertex(1)
our_graph.add_vertex(2)
our_graph.add_vertex(3)
our_graph.add_vertex(4)
our_graph.add_vertex(5)
our_graph.add_vertex(6)
our_graph.add_vertex(7)

# make connections to neighbors
our_graph.add_edges(1,2)
our_graph.add_edges(2,3)
our_graph.add_edges(2,4)
our_graph.add_edges(3,5)
our_graph.add_edges(4,6)
our_graph.add_edges(4,7)
our_graph.add_edges(5,3)
our_graph.add_edges(6,3)
our_graph.add_edges(7,1)
our_graph.add_edges(7,6)

# start testing 
print('--------------------')
print('The verticies of our graph are:', our_graph.verticies)
print('The neighbors of 7 are:', our_graph.get_neighbors(7))
print('The following is the full Breadth First Traveral graph:')
our_graph.bft(1)
print('The following is the full Depth First Traversal graph:')
our_graph.dtf(1)
print('The following is the full Breadth First Search graph', our_graph.bfs(1,6))
print('--------------------')

