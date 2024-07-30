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










    
 
