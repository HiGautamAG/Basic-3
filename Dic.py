# Dictionary are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

# Example:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


info = {
    "name": "Ansh",
    "Subjects": ["Python", "JS", "CSS", "HTML"],
    "age": 21,
    "city": "Lucknow",
    "is_adult" : True,
    
}


info["name"] = "Gautam"
info["surname"] = "Ansh"
print(type(info))
print(info["name"])



# null dictionary  

null_dict = {}
null_dict["name"] = "Ansh"
null_dict["surname"] = "Gautam"

print(null_dict)


# Nested Dictionary

nested_dict = {
    "name": "Ansh",
    "subjects":{
        "python" : 65,
        "JavaScript" : 70,
        "CSS" : 60,
        "HTML" : 70,
        }
}


print(nested_dict["subjects"])   # Accessing the nested dictionary 
print(nested_dict["subjects"]["python"])  # Accessing the nested dictionary value
print(list(nested_dict.keys())) # keys() method is used to return the keys of the dictionary
print(len(nested_dict))  # len() method is used to return the length of the dictionary
print(nested_dict.values())  # values() method is used to return the values of the dictionary
print(nested_dict.items())  # items() method is used to return the key-value pair
print(nested_dict.get("name"))  # get() method is used to access the value of the key
print(nested_dict.pop("name"))  # pop() method is used to remove the key-value pair  
print(nested_dict)
print(nested_dict.popitem())  # popitem() method is used to remove the last inserted key-value pair
print(nested_dict.update( {"city": "Lucknow", "age":21}))  # update() method is used to update the dictionary 


# Dictionary Methods   
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair etc......
# update()	Updates the dictionary with the specified key-value pairs


# sets in python
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets.
# sets only store boolean values, integers, float, strings, tuples, etc.


collection = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(collection)   
print(type(collection))  # <class 'set'>


collection = {}

print(type(collection))  # <class 'dict'>



#set mutable but the elements of the set are immutable

# set methods (add(), clear(), copy(), difference(), difference_update(), discard(), intersection(),
# intersection_update(), isdisjoint(), issubset(), issuperset(), pop(), remove(), symmetric_difference(), 
# symmetric_difference_update(), union(), update())
# add()	Adds an element to the set



collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Ansh")
collection.add("1, 2, 3")  
# collection.add([1, 2, 3])  # TypeError:immutable unhashable type: 'list'

print(collection)
print(type(collection))  # <class 'set'>
collection.remove(1)
collection.clear()



collection = {"python", "java", "c++", "c"}
print(collection.pop())  # pop() method is used to remove the last element of the set
print(collection.pop())

# set union  (|) operator is used to perform the union operation


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1)
print(set2)


# set intersection (&) operator is used to perform the intersection operation   

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5}

print(set1. intersection(set2))  # {1, 2, 4, 5}


#practice



dict = {
     "cat" : " A small animal",
     "table" : "A piece of furniture",
     
     
}

print(dict)


subject = { "python", "java", "c++", "c"
           "python", "java", "c++", "c"
           }

print(len(subject))  # {'java', 'c', 'python', 'c++'}




collection = {9, "9.0", 9.0}

print(collection)  # {9}


values ={
    ("float", 1.0),
    ("int", 1),
    ("string", "1")
}

print(values)  # {('int', 1), ('string', '1'), ('float', 1.0)}



marks ={}
user = int(input("Enter Number : "))
sub = input("Enter Subject : ")
mark = int(input("Enter Number : "))
sub = input("Enter Subject 2 : ")
marks[sub] = mark
print(marks)  # {'python': 65, 'java': 70, 'c++': 60, 'c': 70}



    
 
