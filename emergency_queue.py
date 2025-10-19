class Patient:
    def __init__(self, name: str, urgency: int):
        self.name = name
        self.urgency = urgency
    
    def __repr__(self):
        return f"Patient({self.name}, {self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient: Patient) ->None:
        #adds new patient and restores the min-heap property
        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def remove_min(self) -> Patient:
        #removes and returns the most urgent patient
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        min_patient = self.data[0]
        # move last element to root and heapify down
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return min_patient
    
    def peek(self) -> Patient:
        #returns the most urgent patient without removing them
        if not self.data:
            return None
        return self.data[0]
    
    def print_heap(self) -> None:
        #prints all patients and their urgency
        for patient in self.data:
            print(patient)
    
    def _heapify_up(self, index: int) -> None:
        parent_index = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index: int) -> None:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self._heapify_down(smallest)



# Test your MinHeap class here including edge cases
heap = MinHeap()
patients =[
    Patient("Alice", 5),
    Patient("Bob", 2),
    Patient("Charlie", 8),
    Patient("Diana", 1),
    Patient("Eve", 3)
]

#insert patients
for p in patients:
    heap.insert(p)

print("Heap after insertions:")
heap.print_heap()

print("\nMost urgent patient:")
print(heap.peek())

print("\nRemoving patients in order of urgency:")
while heap.data:
    print(heap.remove_min())

#edge cases
print("\nRemoving from empty heap:")
print(heap.remove_min()) #should return None

print("\nPeeking into empty heap:")
print(heap.peek()) #should return None


#Design Memo:

# Why is a tree appropriate for the doctor structure?
# A tree is ideal becuase it naturally models relationships that work off hierarchies. 
# In a hospital, some doctors may supervise others, creating achain of command.
# Each node can represent a doctor, with the lefrt and right child nodes representing their direct reports. 
# The structure allows easy insertion of new doctors, efficient traversal, and a clear visualization of reporting lines.

# When might a software engineer use preorder, inorder, or postorder traversals?
# Preorder:
# Preorder traversals processses a node before its subordinates, useful for generating top-down reports or printing
# an hierarchy.
# Inorder:
# Inorder Traversals are typically used in binary search trees to access data in sorted order. It is useful when a specific
# ordering of nodes is required, such as generating alphabetical lists of doctors.
# Postorder:
# postorder traversals process subordinates before the node itself, useful for aggregating data, calculating total workloads,
# or concolidating information from a team beofre summarizing at the manager level.

# How do heaps help simulate real-time systems like emergency intake?
# Heaps efficiently maintain a priority queue, which is essential for emergency intake where patients are treated based on urgency
# rather that arrival time. A min-heap allows the patient with the highest priority (lowest urgency score) to be accessed directly are the root.
# inserting new patients and removing the most urgent patient can be done in logarithmic time, making it practical for real-time decision making.
