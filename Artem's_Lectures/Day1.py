'''                 Artem's Lecture  - CSPT11
            https://www.youtube.com/watch?v=XPp_ipD8Mr8&feature=youtu.be
'''

'''
-----Adjaciency Matrix - good for dense/cyclic graphs

2D array visualiztion

verticies = 1,2,3,4,5,6,7

USE THIS FILE FOR PICTURE OF GRAPH
# C:/Users/regin/Documents/GitHub_Repos/Graphs/objectives/breadth-first-search/img/bfs-visit-order.png


    1 2 3 4 5 6 7
  1[F T F F F F F ] Inside the brackets  
  2[              ]  we store information
  3[              ]   about the edges. They
  4[              ]    will be T/F values, 
  5[              ]     yes/no if there are edges
  6[              ]      A good way to find neighbors
  7[              ] 


-----Adjaciency Lists - actually a dictonary - better space complexity
keys = verticies/node values
values = key's node neighbors - set is used here
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


    # searching the graph
    def bfs(self, starting_vertex_id, target_vertex_id):
        '''
        This algorithm does Breadth First Search unitl the goal vertex
        is found. Returns an array of vertex IDs that are part of the PATH.
        '''
        # create an empty queue and ADD a PATH to starting vertex
        # in other words - add array [1] to the queue
        

        # create a visited set of verticies

        # while queue is NOT empty
            # dequeue the current PATH from the queue


            # get the current vertex to analyze from the PATH
            # use the vertex at the END of the PATH array

            # if vertex has not been visited
                # add vertex to visited list

                # check if current vertex is the target vertex
                    # found the vertex and the PATH to it
                    # return the PATH

                # for each neighbor of the current vertex
                    # add the PATH to that neighbor to the queue
                        # COPY  the current PATH
                        # add neightbor to the new path
                        # add the whole PATH to the queue
        pass



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
print('--------------------')


