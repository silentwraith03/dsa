a = [546, 12,213, 123,2, 132312]

# Array assigns index to each element
# Index starts from 0
# Index ends at Length(Array)-1

# len function returns the length of array
print("Length of the array is: {}".format(len(a)))

# function 
# Returns the full output at once
def simpleGeneratorFun():
    return 1          
    return 2           
    return 3     

print(simpleGeneratorFun())
print(simpleGeneratorFun())
print(simpleGeneratorFun())

# generator
# Returns the output one at a time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3     

for value in simpleGeneratorFun():
    print("Happened")
    print(value)

# range function goes from start index to stop index -1 with the step provided in function
print("First element in array: {}".format(a[0]))
print("Last element in array: {}".format(a[-1]))
print("Last element in array: {}".format(a[len(a)-1]))

print("Array in forward")
for i in range(0, len(a), 1):
    print(a[i])

print("Array in reverse")
for i in range(-1, len(a)*(-1), -1):
    print(a[i])

print("Array in reverse")
for i in range(len(a)-1, 0, -1):
    print(a[i])