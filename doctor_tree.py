class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None
    
    def insert(self, parent_name: str, employee_name: str, side: str) -> bool:
        #inserts a new doctor under the specified parent on the given side.
        #returns True if successful, False if not.

        new_node = DoctorNode(employee_name)
        if self.root is None:
            if parent_name is None:
                self.root = new_node
                return True
            else: 
                return False
        # if the tree is empty this will set root if parent name is None

        parent = self._find_node(self.root, parent_name)
        if parent is None:
            return False
        #finding the parent node, returning false if not found

        if side.lower() == 'left':
            if parent.left is None:
                parent.left = new_node
                return True
            else:
                return False
        elif side.lower()=='right':
            if parent.right is None:
                parent.right = new_node
                return True
            else:
                return False
        else:
            return False
        #finding if left or right child already exist returning False if not
        
    def _find_node(self, node: DoctorNode, name: str) -> DoctorNode:
            #finds and returns the node with the given name (doctornode)
        if node is None:
            return None
        if node.name == name: 
            return node
        left_result = self._find_node(node.left, name)
        if left_result:
            return left_result
        return self._find_node(node.right, name)
    #searches the tree recursively for a node with the specified name

    def preorder(self,node: DoctorNode) -> list:
        #returns a list of doctor names in preorder traversal
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    
    def inorder(self, node: DoctorNode) -> list:
        #returns a list of doctor names in inorder traversal
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
    
    def postorder(self, node: DoctorNode) -> list:
        #returns a list of doctor names in postorder traversal
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
    



# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.insert(None, "Dr. Smith", "left")
#root node
tree.insert("Dr. Smith", "Dr. Johnson", "left")
tree.insert("Dr. Smith", "Dr. Lee", "right")
tree.insert("Dr. Johnson", "Dr. Brown", "left")
tree.insert("Dr. Johnson", "Dr. Davis", "right")
tree.insert("Dr. Lee", "Dr. Wilson", "left")
tree.insert("Dr. Lee", "Dr. Taylor", "right")

print("Preorder Traversal:", tree.preorder(tree.root))
print("Inorder Traversal:", tree.inorder(tree.root))
print("Postorder Traversal:", tree.postorder(tree.root))
