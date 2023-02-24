# Hashmap is a data structure that uses key value pairs to store data
# It is generally used to decrese the time complexity of accessing data

class HashMap:
    # __init__() is an initializer/constructor for a class in Python
    # "self" is used to refer to the object created from class
    def __init__(self):
        self.storage={}
    
    # self refers to the object created from class
    def insert(self, data):
        # Inserts a key value pair of (data, 1) in storage dictionary
        self.storage[data]=1

    def show(self):
        # Shows the dictionary used by HashMap class
        print(self.storage)

    def search(self, data):
        # Returns True if data is present in Hashmap
        # Returns False if data is not present in HashMap
        if data in self.storage:
            return True
        return False

hm = HashMap()
hm.insert(1)
hm.insert(2)
hm.insert(3)
hm.insert(4)
hm.insert(5)
hm.insert(6)

print("Hashmap: ")
hm.show()

search_val = 4
print("Check if {} is in hashmap: {}".format(search_val, hm.search(search_val)))