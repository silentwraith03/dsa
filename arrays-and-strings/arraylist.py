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
            for i in range(len(self.storage)):
                if self.storage[i]==None:
                    self.storage[i]=data
                    break
        else:
            self.size = self.size*2
            new_array = [None]*self.size
            print("Size if arraylist: {}".format(len(self.storage)))
            for i in range(len(self.storage)):
                new_array[i]=self.storage[i]
            new_array[i+1]=data
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