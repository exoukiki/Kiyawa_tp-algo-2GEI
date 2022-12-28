import ctypes
class DynamicArray:
    """ A dynamic array class as a simplified Python list """
    def __init__(self):
        """Create an empty array."""
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity)
        # low-level array
    def __len__(self):
        """Return number of elements stored in the array.""" #les elts stockés das le tableau 
        return self._n
    def __getitem__(self, k):
        """Return the item at position k"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k] # retreive from array
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            # not enough room
            self._resize(2*self._capacity)
            # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        """Resize internal array to capacity c"""
        B= self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()
if __name__=='__main__':
    ax= DynamicArray()
    print("Vérifions la taille des éléments")
    print(len(ax))
    ax.append(3)
    print(len(ax))
    print(ax._capacity)
    self.ax
    print(ax._resize)
