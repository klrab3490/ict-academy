# Day 2

## Topics
```
📁 Day 2 - Topics
├── Collection       # Collection types are used to store multiple values.
│   ├── List         # List type, an ordered, mutable collection of elements.
│   │   ├── Define: variable = []
│   │   ├── Get elements using index
│   │   ├── Updation: variable[index] = new_value
│   │   ├── Functions:
│   │   │   ├── Insertions:
│   │   │   │   ├── Append - variable.append(value)             # Add value at the end of the list
│   │   │   │   ├── Insert - variable.insert(index, value)      # Add value at the specified index
│   │   │   │   ├── Extend - variable.extend(another_list)      # Add all elements of another list to the existing list
│   │   │   ├── Count - variable.count(value)                   # Count the number of occurrences of the specified element in the list
│   │   │   ├── Length - len(variable) or variable.__len__()    # Get the number of elements in the list
│   │   │   ├── Deletion:
│   │   │   │   ├── Pop - variable.pop(index)                   # Remove and return the element at the specified index position
│   │   │   │   ├── Remove - variable.remove(element)           # Remove the first occurrence of the specified element
│   │   │   │   ├── Clear - variable.clear() or del variable[:] # Remove all elements in the list
│   │   │   │   ├── Delete - del variable                       # Remove the entire list from memory
|   |   |   ├── Copying - new=variable.copy()                   # To Copy the list 
|   |   |   ├── Assign - new=variable                           # list changes Affect both
│   |
|   ├── Tuples       # Tuple type, an ordered, immutable collection of elements.
│   │   ├── Define: variable = ()
│   │   ├── Get elements using index
│   │   ├── Functions:
│   │   │   ├── Count - variable.count(value)   # Count the occurrences of the specified element
│   │   │   ├── Index - variable.index(value)   # Get the index of the first occurrence of the specified element
|   |
│   ├── Set          # Set type, an unordered collection of unique elements.
│   │   ├── Define: variable = {}
│   │   ├── Add elements: variable.add(value)           # Add a unique element to the set
│   │   ├── Remove elements: variable.remove(value)     # Remove a specified element from the set
|   |
│   ├── Dictionary   # Dictionary type, an unordered collection of key-value pairs.
│   │   ├── Define: variable = {}
│   │   ├── Values Stored as key: value pair            # How its stored
|   |   ├── Access: variable[key]                       # How to acces the value stored at key
│   │   ├── Add or update: variable[key] = value        # Add a new key-value pair or update an existing one
├── User Defined Functions
|   ├── Define: 
```
def function_name(parameters):
    # Function body
    return result

```
|   ├── Function call: function_name(arguments)
|   ├── Get dat On Function: help(function_name)

```