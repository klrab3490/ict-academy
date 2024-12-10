# Day 2

## Topics
```
📁 Day 2 - Topics
├── Collection       # Collection types are used to store multiple values.
│   ├── List         # List type, an ordered, mutable collection of elements.
|   ├── Tuples       # Tuple type, an ordered, immutable collection of elements.
│   ├── Set          # Set type, an unordered collection of unique elements.
│   ├── Dictionary   # Dictionary type, an unordered collection of key-value pairs.
|
├── User Defined Functions
|
├── Class

```

#### List
A **list** is an ordered, mutable collection of elements.

- **Define a List**: 
    ```python
    variable = []
    ```

- **Get Elements**: 
    Access elements using an index.
    ```python
    element = variable[index]
    ```

- **Update Elements**: 
    Update the value at a specific index.
    ```python
    variable[index] = new_value
    ```

- **Functions**:
    - **Insertions**:
        - `append(value)` — Add an element to the end of the list.
          ```python
          variable.append(value)
          ```
        - `insert(index, value)` — Add an element at a specific index.
          ```python
          variable.insert(index, value)
          ```
        - `extend(another_list)` — Add all elements from another list.
          ```python
          variable.extend(another_list)
          ```

    - **Count**: Count the occurrences of a specific value.
      ```python
      count = variable.count(value)
      ```

    - **Length**: Get the number of elements in the list.
      ```python
      length = len(variable)
      ```

    - **Deletions**:
        - `pop(index)` — Remove and return the element at the specified index.
          ```python
          value = variable.pop(index)
          ```
        - `remove(value)` — Remove the first occurrence of an element.
          ```python
          variable.remove(value)
          ```
        - `clear()` — Remove all elements from the list.
          ```python
          variable.clear()
          ```
        - `del` — Delete the entire list.
          ```python
          del variable
          ```

    - **Copying**: Create a copy of the list.
      ```python
      new_list = variable.copy()
      ```

    - **Assignment**: Assignment makes both variables reference the same list.
      ```python
      new_list = variable
      ```

#### Tuple
A **tuple** is an ordered, immutable collection of elements.

- **Define a Tuple**:
    ```python
    variable = ()
    ```

- **Get Elements**: 
    Access elements using an index.
    ```python
    element = variable[index]
    ```

- **Functions**:
    - **Count**: Count the occurrences of a specific value.
      ```python
      count = variable.count(value)
      ```

    - **Index**: Find the index of the first occurrence of a value.
      ```python
      index = variable.index(value)
      ```

#### Set
A **set** is an unordered collection of unique elements.

- **Define a Set**:
    ```python
    variable = set()
    ```

- **Add Elements**: 
    Use `add()` to add a unique element.
    ```python
    variable.add(value)
    ```

- **Remove Elements**: 
    Use `remove()` to remove a specific element.
    ```python
    variable.remove(value)
    ```

#### Dictionary
A **dictionary** is an unordered collection of key-value pairs.

- **Define a Dictionary**:
    ```python
    variable = {}
    ```

- **Accessing Values**: 
    Access the value associated with a specific key.
    ```python
    value = variable[key]
    ```

- **Add or Update**:
    Add new key-value pairs or update existing ones.
    ```python
    variable[key] = value
    ```

---

### User Defined Functions

Functions are defined using the `def` keyword and can be called with specific arguments.

- **Define a Function**:
    ```python
    def function_name(parameters):
        # Function body
        return result
    ```

- **Function Call**:
    To call a function, pass the required arguments.
    ```python
    function_name(arguments)
    ```

- **Get Function Documentation**:
    Use `help()` to view a function's documentation.
    ```python
    help(function_name)
    ```

---

### Class

A **class** is a blueprint for creating objects, defining methods and attributes.

- **Define a Class**:
    ```python
    class class_name:
        def __init__(self):
            # Initialization code
            pass
    ```

- **Create an Object**:
    To create an object of the class, instantiate it like this:
    ```python
    object_name = class_name()
    ```

---

## Summary

- **Collections**: List, Tuple, Set, Dictionary — Useful for grouping and manipulating multiple values.
- **User Defined Functions**: For encapsulating reusable code logic.
- **Classes**: To define the structure of objects and their behavior.
