class node():
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None

    #function to add data to the tree
    def add(self, data):
        if data<=self.data:
            #if left child exists, recurse else make a node
            if not self.left==None:
                self.left.add(data)
            else:
                self.left=node(data)
        else:
            #if right child exists,recurse, else make a node
            if not self.right==None:
                self.right.add(data)
            else:
                self.right=node(data)

    #function to print out the whole tree            
    def display(self, order='in'):
        
        if order=='in':
            if not self.left==None:
                self.left.display(order='in')
                
            print self.data,
            
            if not self.right==None:
                self.right.display(order='in')
                
        elif order=='pre':
            print self.data,
            
            if not self.left==None:
                self.left.display(order='pre')
            
            if not self.right==None:
                self.right.display(order='pre')
                
        elif order=='post':
            if not self.left==None:
                self.left.display(order='post')
            
            if not self.right==None:
                self.right.display(order='post')

            print self.data,
            
        else:
            print 'Invalid order key'