# Filename: max_heap.py

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_val = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            max_val = self.heap.pop()
        else:
            max_val = None
        return max_val

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Usage Example
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
print(heap.get_max())  # Output: 20
print(heap.delete())  # Output: 20
print(heap.get_max())  # Output: 10
