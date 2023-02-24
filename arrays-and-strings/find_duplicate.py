# Problem: To find if an array has a duplicate element.
# Implement a function has_duplicate which returns True if array has duplicate element and False otherwise.

# Brute Force Solution
# def has_duplicate(array):
#     for index1 in range(len(array)):
#         element1 = array[index1]
#         for index2 in range(index1+1, len(array)):
#             element2 = array[index2]
#             if element1==element2:
#                 return True
#     return False

class HashMap:
    def __init__(self):
        self.storage={}
    
    def insert(self, data):
        self.storage[data]=1
    
    def search(self, data):
        if data in self.storage:
            return True
        else:
            return False

# Relatively Optimzied Solution
def has_duplicate(array):
    hm = HashMap()
    
    # For every element in array
    for index in range(len(array)):
        
        # If element is already present in HashMap
        # Then we have encontered a duplicate
        if hm.search(array[index])==True:
            return True
        
        # If element is not present in HashMap
        # Then add the element in HashMap
        else:
            hm.insert(array[index])
            
    return False
    
    
array = [1, 23, 213, 123, 123]
print("Check if array has duplicate: {}".format(has_duplicate(array)))

array2 = [1, 23, 213, 123]
print("Check if array has duplicate: {}".format(has_duplicate(array2)))