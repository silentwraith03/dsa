# Arraylist is a data structure that is similar to array
# But it doubles its size everytime it runs out of space

class ArrayList:
    def __init__(self, size):
        self.size=size
        self.storage=[None]*self.size

    def insert(self, data):
        # Checks if the last element is None
        #      Loops over array
        #        Inserts element at first None position encountered
        # If arraylist is full
        #        Double the size of array list
        #        Create a new array twice the size
        #        Loops over original array
        #           Copies element to new array
        #        Inserts element at first None position
        if self.storage[-1]==None:
            for index in range(len(self.storage)):
                if self.storage[index]==None:
                    self.storage[index]=data
                    break
        else:
            self.size = self.size*2
            new_array = [None]*self.size
            
            # Copying elements from old storage array to new storage array
            for index in range(len(self.storage)):
                new_array[index]=self.storage[index]
            
            # Insert the new element
            new_array[index+1]=data
            
            # Updated the storage
            self.storage=new_array            
    
    def show(self):
        print(self.storage)

al = ArrayList(5)
al.insert(3)
al.insert(2)
al.insert(4)
al.insert(56)
al.insert(3)
al.insert(3)

print("ArrayList:")
al.show()