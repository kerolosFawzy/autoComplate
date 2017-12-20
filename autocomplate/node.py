

def fileparse(filename):

    fd = open(filename)

    root = Node()
    line = fd.readline().strip('\r\n')

    while line != '':
        root.add_item(line) 
        line = fd.readline().strip('\r\n')

    return root

class Node:

    def __init__(self):
        self.next = {}
        self.boolean = False

    #This method to add a string the Trie data structure
    def add_item(self, string):

        if len(string) == 0:
            self.boolean = True
            return

        key = string[0]  # get first character from string

        string = string[1:]  # Create a string by removing first character

        # If the key character exists in the hash, call next pointing node's add_item() with
        # remaining string (re)

        if self.next.has_key(key):
            self.next[key].add_item(string)

        # Else create an empty node. Insert the key character to hash and point it to newly created node.
        # Call add_item() in new node with remaining string.
        else:
            node = Node()
            self.next[key] = node
            node.add_item(string)

    #Depth First Search Traversal
    def dfs(self, sofar=None):


        # When hash of the current node is empty, that means it is a leaf node.


        if self.next.keys() == []:
            print "Match:", sofar
            return

        if self.boolean == True:
            print "Match:", sofar

        # Recursively call dfs for all the nodes pointed by keys in the hash

        for key in self.next.keys():
            self.next[key].dfs(sofar + key)

    def search(self, string, sofar=""):
        '''Perform auto completion search and print the autocomplete results'''
        # Make state transition based on the input characters.

        # When the input characters becomes exhaused, perform dfs() so that the trie gets traversed upto leaves and print the state characters

        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if self.next.has_key(key):
                sofar = sofar + key
                self.next[key].search(string, sofar)

            else:
                print "No match"
        else:
            if self.boolean == True:
                print "Match:", sofar

            for key in self.next.keys():
              self.next[key].dfs(sofar + key)

