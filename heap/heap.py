class Heap:
    def __init__(self, list, airty):
        self._list = list.copy()
        self._airty = airty
        for i in range((len(self._list) // self._airty)-1, -1, -1):
            self.heapify(len(self._list), i)

    def get_list(self):
        return self._list

    def get_airty(self):
        return self._airty

    def get_root(self):
        # Returns value of the root
        if self.get_list() == []:
            raise ValueError("Nothing in the heap!")
        return self.get_list()[0]

    def print(self):
        # Prints whole heap
        self.print_with_children(0, 0)

    def print_with_children(self, index, depth):
        # Prints chosen node with all children
        list_of_tabs = []
        for i in range(depth):
            list_of_tabs.append('\t')
        list_of_tabs = "".join(list_of_tabs)
        print(f"{list_of_tabs}{self.get_list()[index]}")
        depth += 1
        for child in self.get_children(index):
            self.print_with_children(child, depth)

    def size(self):
        # Returns length of the list
        return len(self.get_list())

    def get_children(self, index):
        # Returns list of node's children's indexes, which are on the heap
        children = []
        for i in range(1, self.get_airty() + 1):
            pot = index * self.get_airty() + i
            if not pot > len(self.get_list()) - 1:
                children.append(index * self.get_airty() + i)
        return children

    def get_parent(self, index):
        # Returns node's parent's index
        if index == 0:
            return -1
            #raise ValueError("Root can't have parents!")
        return (index - 1) // self.get_airty()

    
    def heapify(self, n, i):
        largest = i
        children = self.get_children(i)

        for child in children:
            if child <= n and self._list[largest] < self._list[child]:
                largest = child
        
        if largest != i:
            self._list[i], self._list[largest] = self._list[largest], self._list[i]
            self.heapify(n, largest)
        else:
            return -1


    def insert(self, new_element):
        size = len(self._list)
        if size == 0:
            self._list.append(new_element)
        else:
            self._list.append(new_element)
            size += 1

            parent = self.get_parent(size-1)
            stop_parent = parent
            end = False
            while end is False:

                stop_parent = self.get_parent(stop_parent)
                if self._list[size - 1] < self._list[stop_parent]:
                    end = True

                if stop_parent == 0:
                    end = True

            while parent >= stop_parent:
                self.heapify(size + 1, parent)
                parent = self.get_parent(parent)

    def remove_root(self):
        size = len(self._list)
        if size == 0:
            return
        else:
            root = 0

            self._list[root], self._list[size-1] = self._list[size-1], self._list[root]
            self._list.pop()
            size -=1

            self.heapify(size + 1, 0)
                
