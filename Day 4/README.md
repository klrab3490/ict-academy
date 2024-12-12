# Day 3 - Tkinter

## Topics
- **Modules**
    - **Numpy**
    - **glob**
    - **pillow**
    - **array**
---


### 1. **NumPy Array Functions**
NumPy is a powerful library used for numerical computing in Python. Here's how to use some of its functions:

#### - `filter()`
In Python, `filter()` is used to filter elements from an iterable based on a function.

```python
# Example: filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

#### - `map()`
The `map()` function is used to apply a function to all items in an input list (or any other iterable).

```python
# Example: square each number in a list
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
```

#### - `numpy.shape`
`shape` is used to get the dimensions of a NumPy array.

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3) (2 rows, 3 columns)
```

#### - `numpy.reshape()`
`reshape()` is used to change the shape of an array without changing its data.

```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))  # Reshaping to a 2x3 array
print(reshaped_arr)
```

#### - `numpy.transpose()`
`transpose()` is used to swap the dimensions of a NumPy array.

```python
arr = np.array([[1, 2], [3, 4]])
transposed_arr = arr.transpose()
print(transposed_arr)
```

#### - `numpy.where()`
`where()` is used to return elements based on a condition.

```python
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3, 'greater', 'lesser')
print(result)  # Output: ['lesser' 'lesser' 'lesser' 'greater' 'greater']
```

### 2. **Array Views and Copies**

#### - `array.view()`
A view is a new array object that looks at the same data as the original array.

```python
arr = np.array([1, 2, 3, 4, 5])
view_arr = arr.view()
view_arr[0] = 10
print(arr)  # Output: [10, 2, 3, 4, 5] (view affects the original array)
```

#### - `array.copy()`
A copy creates a new array with its own data, independent of the original array.

```python
arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()
copy_arr[0] = 10
print(arr)  # Output: [1, 2, 3, 4, 5] (original array is unaffected)
```

### 3. **Working with Images**
The `PIL` (Pillow) library allows for handling images in Python. You can use `Image` and `ImageTk` to handle image files and display them in a GUI.

#### - `Image` and `ImageTk`
To load, manipulate, and display images using `Pillow` (PIL):

```python
from PIL import Image, ImageTk
import tkinter as tk

# Open an image file
image = Image.open("path_to_image.jpg")

# Convert to a Tkinter-compatible photo object
tk_image = ImageTk.PhotoImage(image)

# Create a Tkinter window to display the image
root = tk.Tk()
label = tk.Label(root, image=tk_image)
label.pack()
root.mainloop()
```

#### - `glob``
The `glob` module is used for matching file path patterns. It's commonly used to retrieve filenames from directories that match a specific pattern.

```python
import glob
files = glob.glob("*.txt")
print(files)  # Returns all .txt files in the current directory
```

#### - `os``
The `os` module allows interaction with the operating system. It is commonly used for file and directory management, such as creating, removing, and changing directories, and handling file paths.

```python
import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

# List all files in a directory
files = os.listdir(current_directory)
print(files)
```

### 4. **Complete Example with NumPy and Images**

Combining everything in a single example:

```python
import numpy as np
from PIL import Image
import glob
import os

# Example of NumPy array manipulations
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(f"Reshaped Array:\n{reshaped_arr}")

# Example of image loading
image_path = "path_to_image.jpg"
image = Image.open(image_path)

# Convert the image to grayscale and display
gray_image = image.convert("L")
gray_image.show()

# Use glob to get all .jpg files in a folder
image_files = glob.glob(os.path.join("path_to_directory", "*.jpg"))
print("Image Files:", image_files)
```

This will demonstrate the manipulation of arrays with NumPy and loading and processing images using the Pillow library.

