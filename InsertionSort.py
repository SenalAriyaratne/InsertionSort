class InsertionSort:
    def __init__ (self, array):
        self._key_index = 1
        self._array_to_sort = array
    
    def _swap(self, i, j):
       # self.array[i], self.array[j] = self.array[j], self.array[i]
       self._array_to_sort[i], self._array_to_sort[j] = self._array_to_sort[j], self._array_to_sort[i]
    
    def print_array(self):
        print(self._array_to_sort)
    
    def return_array(self):
        return self._array_to_sort

    def sort(self):
        for j in range(1, len(self._array_to_sort)):
            key = self._array_to_sort[j]
            i = j - 1
            while i >= 0 and self._array_to_sort[i] > key:
               # self._array_to_sort[i + 1] = self._array_to_sort[i]
               self._swap(i, i + 1)
               i = i - 1
            self._array_to_sort[i + 1] = key
