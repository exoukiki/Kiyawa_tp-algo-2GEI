"""author:MWALI ET KIYAWA"""

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
        """Return number of elements stored in the array."""
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
if __name__ =="__main__":
    jacob = DynamicArray()
    print("passons à la verification de nos fonctions")
    print("le tableau actuel possede {} élements avec une capacité élementaire de {} ".format(jacob._n, jacob._capacity))
    # ainsi nous pouvons definir notre nouvelle liste 
    for i in range(40):
        jacob.append(i)
    print("Ce nouveau tableau contient {} éléments, avec une capacité de {}".format(len(jacob), jacob._capacity))
    #utilisons le __gititem__ et cherchons maintement la position d'un élément dans notre tableau
    print("L'élément qui a l'index 20 est {}".format(jacob.__getitem__(21)))
    # notre tableau possede 40 éléments avec une capacité de 42
    jacob.append(60)
    print("Le nombre d'élément du tableau est ",jacob._n,"mais la capacité est toujours égale à", jacob._capacity )
    jacob.append(0)
    jacob.append(5)
    print("Le nombre d'éléments dans le tableau est",jacob._n,"et la nouvelle capacité devient égale à", jacob._capacity )
    #Essayons maintenant de modifier la capacité de notre tableau pour que qu'elle devienne de 45
    jacob._resize(45)
    print("Le nombre d'éléments dans le tableau est",jacob._n,", et la nouvelle capacité devient égale à", jacob._capacity )
    # créons un tableau quelconque avec une capacité quelconque
    
    print("{}".format(jacob._make_array(20)))
   
    
    
