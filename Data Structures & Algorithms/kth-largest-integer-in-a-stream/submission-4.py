class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k + 1 # first index of heap is ignored
        self._numbers = nums
        self._min_heap = [0]
        self._heapify()

    def add(self, val: int) -> int:
        self._numbers.append(val)
        self._heap_push(val)
        print(self._min_heap)
        if len(self._min_heap) > self._k:
                self._heap_pop()
        
        print(self._min_heap)
        return self._min_heap[1]

    def _heapify(self):
        # Construct the heap from scratch
        for i in range(len(self._numbers)):
            self._heap_push(self._numbers[i])
            if len(self._min_heap) > self._k:
                self._heap_pop()

        print(self._min_heap)
    
    def _heap_push(self, val: int):
        self._min_heap.append(val)
        curr =  len(self._min_heap) - 1
        parent = curr // 2

        while curr > 1 and self._min_heap[curr] < self._min_heap[parent]:
            tmp = self._min_heap[parent]
            self._min_heap[parent] = self._min_heap[curr]
            self._min_heap[curr] = tmp

            curr = parent
            parent = curr // 2
    
    def _heap_pop(self):
        length = len(self._min_heap)
        if length == 1:
            return None
        if length == 2:
            self._min_heap.pop()
            return

        # Min number = self._min_heap[1]
        self._min_heap[1] = self._min_heap.pop()

        i = 1
        new_length = length - 1
        while True:
            left = 2 * i
            right = left + 1
            smaller = i
            
            if right < new_length and self._min_heap[right] < self._min_heap[smaller]:
                smaller = right
            
            if left < new_length and self._min_heap[left] < self._min_heap[smaller]:
                smaller = left

            if smaller != i:
                self._min_heap[smaller], self._min_heap[i] = self._min_heap[i], self._min_heap[smaller]
                i = smaller
            else:
                break


