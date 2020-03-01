class Node(object):
    '''
    builded a singly linked node.

    '''

    def __init__(self, data, next=None):
        '''Instantiates a None with a default next of Node.'''
        self.data = data
        self.next = next
