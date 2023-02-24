# HashMap counter is a data structure that stores the count of occurances of a character
# Input: "abcbcbcbccc"
# Output: {
#     "a":1,
#     "b":4,
#     "c":6
# }

class HashMapCounter:
    def __init__(self):
        self.hashmap = {}

    def insert(self,input_str):
        for index in range(len(input_str)):
            character = input_str[index] 
            
            # If character is already present in hashmap
            #   Increment the count by 1
            if character in self.hashmap: 
                # count = self.hashmap[character]
                # count = count + 1
                # self.hashmap[character] = count 
                
                self.hashmap[character] += 1
            
            # If character is not present in hashmap
            # Insert the character with count = 1
            else:
                self.hashmap[character]=1
    
    def show(self):
        print(self.hashmap)
        

input_string="abcbcbcbccc"
hmc = HashMapCounter()
hmc.insert(input_string)

hmc.show()

input_string="awervihnuwiervghuevthnjio"
hmc2 = HashMapCounter()
hmc2.insert(input_string)

hmc2.show()