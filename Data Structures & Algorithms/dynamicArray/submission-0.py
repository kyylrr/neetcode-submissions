class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0 :
            self.capacity = capacity
            self.my_list = [0] * capacity
            self.size = 0
        
        
    def get(self, i: int) -> int:
       return self.my_list[i] 

    def set(self, i: int, n: int) -> None:
         self.my_list[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.my_list[self.size] = n
        self.size +=1

    def popback(self) -> int:
        last = self.my_list[self.size - 1]
        self.size -= 1
        return last

    def resize(self) -> None:
        self.capacity *= 2
        new_list = [0] * self.capacity
        for i in range(self.size):
            new_list[i] = self.my_list[i]
        self.my_list = new_list

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity